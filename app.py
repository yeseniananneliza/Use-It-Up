import streamlit as st
from recipes_data import RECIPES, ALL_INGREDIENTS

st.set_page_config(page_title="PantryMatch", page_icon="🥕", layout="centered")


# Header

st.title("🥕 PantryMatch")
st.caption("Tell it what's in your kitchen — it tells you what to cook, "
           "prioritizing what's about to go bad.")

with st.expander("Why this exists"):
    st.markdown(
        """
**Problem:** People (me included) overspend on groceries and throw out food
because they don't have a fast way to see *"what can I actually make with
what I already have?"* at the moment they're deciding what to eat.

**v1 scope:** A recipe matcher that ranks meals by how many ingredients you
already have, and pushes recipes using soon-to-expire items to the top —
the highest-leverage slice of the idea, cut down from a larger feature set
(barcode scanning, price tracking, grocery-list generation) that wasn't
necessary to test the core loop.

**What I'd add next:** persistent pantry storage, a real recipe API instead
of a hand-curated list, and a "generate my grocery list" step for whatever's
still missing.
        """
    )

st.divider()


# Pantry input

st.subheader("1. What's in your kitchen?")
have = st.multiselect(
    "Select everything you currently have on hand",
    options=ALL_INGREDIENTS,
    default=["egg", "garlic", "onion", "rice", "cheese"],
)

st.subheader("2. Anything about to go bad?")
expiring = st.multiselect(
    "Select items you need to use up soon (optional)",
    options=have,
)

st.divider()


# Matching logic

have_set = set(have)
expiring_set = set(expiring)

results = []
for r in RECIPES:
    needed = set(r["ingredients"])
    matched = needed & have_set
    missing = needed - have_set
    uses_expiring = needed & expiring_set
    match_pct = round(100 * len(matched) / len(needed)) if needed else 0
    results.append({
        **r,
        "matched": matched,
        "missing": missing,
        "uses_expiring": uses_expiring,
        "match_pct": match_pct,
    })

# Rank: recipes that rescue expiring items float to the top, then by match %
results.sort(key=lambda r: (-len(r["uses_expiring"]), -r["match_pct"]))


# Results

st.subheader("3. What to cook")

if expiring_set:
    rescued = {r["name"] for r in results if r["uses_expiring"]}
    if rescued:
        st.success(
            f"{len(rescued)} recipe(s) below use up items you're about to waste."
        )
    else:
        st.warning(
            "No recipes in this dataset use your expiring items — that's a real "
            "gap a v2 recipe API would close."
        )

shown = [r for r in results if r["match_pct"] > 0]
if not shown:
    st.info("No matches yet — add a few more pantry items above.")

for r in shown[:8]:
    badge = " 🔴 uses expiring item" if r["uses_expiring"] else ""
    with st.container(border=True):
        st.markdown(f"**{r['name']}** · {r['match_pct']}% match · {r['time_minutes']} min{badge}")
        st.caption(", ".join(t.title() for t in r["tags"]))
        if r["missing"]:
            st.markdown(f"🛒 Missing: {', '.join(sorted(r['missing']))}")
        else:
            st.markdown("✅ You have everything for this one.")
        with st.expander("Instructions"):
            st.write(r["instructions"])

st.divider()
st.caption(
    "PantryMatch v1 — built as a scoped product case study. "
    "Dataset: 15 hand-curated recipes. Next iteration: real recipe API + "
    "persistent pantry."
)
