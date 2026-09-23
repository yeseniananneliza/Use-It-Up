import streamlit as st
from recipes_data import RECIPES, ALL_INGREDIENTS

st.set_page_config(page_title="Use It Up", layout="centered")


# Styling: warm, soft, recipe-blog aesthetic

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Nunito:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .stApp {
        background-color: #FBF3EA;
        color: #4A3F35;
    }

    h1 {
        font-family: 'Playfair Display', serif !important;
        color: #B4694A !important;
        font-weight: 700 !important;
    }

    h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #6B5B4E !important;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #8A7A6D;
        font-style: italic;
        margin-top: -0.6rem;
        margin-bottom: 1.2rem;
    }

    /* Recipe cards */
    .recipe-card {
        background-color: #FFFDFB;
        border: 1px solid #F0DFCF;
        border-radius: 16px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 2px 10px rgba(180, 105, 74, 0.08);
    }
    .recipe-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem;
        color: #6B5B4E;
        font-weight: 700;
    }
    .recipe-meta {
        color: #A68F7C;
        font-size: 0.9rem;
        margin-bottom: 0.4rem;
    }
    .tag-pill {
        display: inline-block;
        background-color: #F3E5D8;
        color: #8A6A4E;
        border-radius: 999px;
        padding: 2px 10px;
        font-size: 0.78rem;
        margin-right: 6px;
        margin-bottom: 4px;
    }
    .expiring-pill {
        display: inline-block;
        background-color: #F6D9C8;
        color: #B4694A;
        border-radius: 999px;
        padding: 2px 10px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    .missing-text {
        color: #A68F7C;
        font-size: 0.92rem;
    }
    .ready-text {
        color: #7E9C7A;
        font-size: 0.92rem;
        font-weight: 600;
    }

    /* Soften Streamlit's default multiselect tags */
    span[data-tag] {
        background-color: #D9A98C !important;
        border-radius: 999px !important;
    }

    /* Expander header */
    .streamlit-expanderHeader {
        font-family: 'Nunito', sans-serif;
        color: #6B5B4E;
    }

    /* Buttons / inputs */
    div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        border-color: #E8D3BF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("Use It Up")
st.markdown(
    '<div class="subtitle">A recipe matcher that tells you what to cook with '
    "what's already in your kitchen, prioritizing ingredients about to "
    "expire.</div>",
    unsafe_allow_html=True,
)

with st.expander("Why this exists"):
    st.markdown(
        """
**Problem:** People (me included) overspend on groceries and throw out food
because they don't have a fast way to see *"what can I actually make with
what I already have?"* at the moment they're deciding what to eat.

**v1 scope:** A recipe matcher that ranks meals by how many ingredients you
already have, and pushes recipes using soon-to-expire items to the top,
the highest-leverage slice of the idea, cut down from a larger feature set
(barcode scanning, price tracking, grocery-list generation) that wasn't
necessary to test the core loop.

**What I'd add next:** persistent pantry storage, a real recipe API instead
of a hand-curated list, and a "generate my grocery list" step for whatever's
still missing.
        """
    )

st.divider()

# ---------------------------------------------------------------------------
# Pantry input
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Matching logic
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
st.subheader("3. What to cook")

if expiring_set:
    rescued = {r["name"] for r in results if r["uses_expiring"]}
    if rescued:
        st.success(
            f"{len(rescued)} recipe(s) below use up items you're about to waste."
        )
    else:
        st.warning(
            "No recipes in this dataset use your expiring items, that's a real "
            "gap a v2 recipe API would close."
        )

shown = [r for r in results if r["match_pct"] > 0]
if not shown:
    st.info("No matches yet, add a few more pantry items above.")

for r in shown[:8]:
    tags_html = "".join(f'<span class="tag-pill">{t.title()}</span>' for t in r["tags"])
    expiring_html = '<span class="expiring-pill">Uses expiring item</span>' if r["uses_expiring"] else ""
    if r["missing"]:
        status_html = f'<div class="missing-text">Missing: {", ".join(sorted(r["missing"]))}</div>'
    else:
        status_html = '<div class="ready-text">You have everything for this one</div>'

    st.markdown(
        f"""
        <div class="recipe-card">
            <div class="recipe-title">{r['name']}</div>
            <div class="recipe-meta">{r['match_pct']}% match &middot; {r['time_minutes']} min</div>
            {tags_html} {expiring_html}
            <div style="margin-top:0.5rem;">{status_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.expander(f"Instructions for {r['name']}"):
        st.write(r["instructions"])

st.divider()
st.caption(
    "Use It Up v1, built as a scoped product case study. "
    "Dataset: 15 hand-curated recipes. Next iteration: real recipe API and "
    "persistent pantry."
)
