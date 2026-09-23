import streamlit as st
from recipes_data import RECIPES, ALL_INGREDIENTS

st.set_page_config(page_title="Use It Up", layout="wide")

# ---------------------------------------------------------------------------
# Styling: warm, soft, recipe-blog aesthetic
# ---------------------------------------------------------------------------
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
        margin-bottom: 1.4rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F6E9DC !important;
        border-right: 1px solid #EBD6C2;
    }
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #6B5B4E !important;
    }

    /* Step labels inside sidebar */
    .step-label {
        font-family: 'Playfair Display', serif;
        font-size: 1.15rem;
        color: #6B5B4E;
        font-weight: 700;
        margin-top: 1.2rem;
        margin-bottom: 0.1rem;
    }
    .step-help {
        color: #A68F7C;
        font-size: 0.85rem;
        margin-bottom: 0.4rem;
    }

    /* Recipe cards */
    .recipe-card {
        background-color: #FFFDFB;
        border: 1px solid #F0DFCF;
        border-radius: 16px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 0.7rem;
        box-shadow: 0 2px 10px rgba(180, 105, 74, 0.08);
        min-height: 168px;
    }
    .recipe-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        color: #6B5B4E;
        font-weight: 700;
    }
    .recipe-meta {
        color: #A68F7C;
        font-size: 0.88rem;
        margin-bottom: 0.4rem;
    }
    .tag-pill {
        display: inline-block;
        background-color: #F3E5D8;
        color: #8A6A4E;
        border-radius: 999px;
        padding: 2px 10px;
        font-size: 0.76rem;
        margin-right: 6px;
        margin-bottom: 4px;
    }
    .expiring-pill {
        display: inline-block;
        background-color: #F6D9C8;
        color: #B4694A;
        border-radius: 999px;
        padding: 2px 10px;
        font-size: 0.76rem;
        font-weight: 700;
    }
    .missing-text {
        color: #A68F7C;
        font-size: 0.88rem;
    }
    .ready-text {
        color: #7E9C7A;
        font-size: 0.88rem;
        font-weight: 600;
    }

    /* Expanders (instructions, everywhere): force warm styling in every state */
    div[data-testid="stExpander"] {
        background-color: #F6E9DC !important;
        border: 1px solid #EBD6C2 !important;
        border-radius: 14px !important;
        margin-bottom: 0.5rem !important;
    }
    div[data-testid="stExpander"] > details {
        background-color: #F6E9DC !important;
        border-radius: 14px !important;
    }
    div[data-testid="stExpander"] summary {
        background-color: #F6E9DC !important;
        font-family: 'Nunito', sans-serif !important;
        font-weight: 700 !important;
        color: #8A6A4E !important;
        border-radius: 14px !important;
    }
    div[data-testid="stExpander"] summary svg {
        fill: #8A6A4E !important;
    }
    div[data-testid="stExpanderDetails"] {
        background-color: #FFFDFB !important;
        color: #4A3F35 !important;
    }

    /* Multiselect tags */
    span[data-tag] {
        background-color: #D9A98C !important;
        border-radius: 999px !important;
    }

    /* Multiselect / select input box itself, hard-coded so it never falls back to dark */
    div[data-baseweb="select"] > div {
        background-color: #FFFDFB !important;
        border-radius: 12px !important;
        border-color: #E8D3BF !important;
    }
    div[data-baseweb="select"] input {
        color: #4A3F35 !important;
    }
    ul[role="listbox"] {
        background-color: #FFFDFB !important;
    }
    ul[role="listbox"] li {
        color: #4A3F35 !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.05rem !important;
        color: #A68F7C !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #B4694A !important;
    }
    div[data-baseweb="tab-highlight"] {
        background-color: #B4694A !important;
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

# ---------------------------------------------------------------------------
# Sidebar: pantry input (always visible, out of the way of the main content)
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### Your Kitchen")

    st.markdown('<div class="step-label">What do you have?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="step-help">Select everything you currently have on hand</div>',
        unsafe_allow_html=True,
    )
    have = st.multiselect(
        "Pantry items",
        options=ALL_INGREDIENTS,
        default=["egg", "garlic", "onion", "rice", "cheese"],
        label_visibility="collapsed",
    )

    st.markdown('<div class="step-label">Anything about to go bad?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="step-help">Optional, prioritizes recipes that use these up</div>',
        unsafe_allow_html=True,
    )
    expiring = st.multiselect(
        "Expiring items",
        options=have,
        label_visibility="collapsed",
    )

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
# Tabs
# ---------------------------------------------------------------------------
cook_tab, about_tab = st.tabs(["What to Cook", "About This Project"])

with cook_tab:
    if expiring_set:
        rescued = {r["name"] for r in results if r["uses_expiring"]}
        if rescued:
            st.success(
                f"{len(rescued)} recipe(s) below use up items you're about to waste."
            )
        else:
            st.warning(
                "No recipes in this dataset use your expiring items, that's a "
                "real gap a v2 recipe API would close."
            )

    shown = [r for r in results if r["match_pct"] > 0]
    if not shown:
        st.info("No matches yet, add a few more pantry items in the sidebar.")

    # Responsive-ish grid: 3 cards per row
    cards_per_row = 3
    for row_start in range(0, min(len(shown), 9), cards_per_row):
        row = shown[row_start:row_start + cards_per_row]
        cols = st.columns(cards_per_row)
        for col, r in zip(cols, row):
            with col:
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
                    st.markdown(f"**Serves {r.get('servings', 2)}**")
                    st.markdown("**Ingredients:**")
                    for ing in r["ingredients"]:
                        amount = r.get("amounts", {}).get(ing, "")
                        line = f"- **{ing.title()}:** {amount}" if amount else f"- {ing.title()}"
                        st.markdown(line)
                    st.markdown("**Steps:**")
                    for i, step in enumerate(r.get("steps", []), start=1):
                        st.markdown(f"{i}. {step}")

    st.divider()
    st.caption(
        "Use It Up v1, built as a scoped product case study. "
        "Dataset: 15 hand-curated recipes. Next iteration: real recipe API and "
        "persistent pantry."
    )

with about_tab:
    left, right = st.columns([2, 1])
    with left:
        st.markdown(
            """
### Why this exists

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
    with right:
        st.markdown(
            """
            <div class="recipe-card">
                <div class="recipe-title">At a glance</div>
                <div class="recipe-meta">15 hand-curated recipes</div>
                <div class="recipe-meta">Matches by ingredient overlap</div>
                <div class="recipe-meta">Prioritizes expiring items</div>
                <div class="recipe-meta">Built in a single day, scoped on purpose</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
