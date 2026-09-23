# PantryMatch

A minimal recipe matcher: tell it what's in your kitchen, it ranks recipes by
match %, and surfaces the ones that use up ingredients you're about to waste.

Built as a scoped product case study: problem framing, prioritization, and a
v1 build in a day rather than a polished/complete product.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Opens at http://localhost:8501

## Deploy for free (so you have a live link for your portfolio/resume)
1. Create a new GitHub repo (e.g. `pantrymatch`) and push these three files:
   `app.py`, `recipes_data.py`, `requirements.txt`.
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with
   GitHub, click **New app**, point it at the repo and `app.py`.
3. Deploy — you'll get a live URL like `pantrymatch.streamlit.app` in a
   couple minutes. That's the link to put in your portfolio and resume.

## What's scoped out of v1 (intentionally)
- Persistent pantry storage (currently resets each session)
- A real recipe API (Spoonacular/Edamam) instead of the 15 hand-curated recipes
- Auto-generated grocery list for missing ingredients
- Barcode/receipt scanning for pantry input

These are the natural v2 roadmap, cut from v1 to validate the core loop fast.
