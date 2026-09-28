# Use It Up

Tell it what's in your kitchen and it finds recipes you can make now, starting with the food that's about to go bad.

**Live site:** https://yeseniananneliza.github.io/Use-It-Up/

## What it does
- Add ingredients you have and mark anything that needs to be used soon
- 25 recipes across 14 cuisines, ranked so recipes that rescue expiring food come first
- Full recipe pages with measurements, stove and oven settings, a servings scaler and step-by-step directions
- A grocery list that combines what's missing across every recipe you plan to cook
- Your kitchen and list are saved in your browser

## Built with
Plain HTML, CSS and JavaScript in a single file (`index.html`), no framework and no backend. `app.py` serves the same file on Streamlit Community Cloud.

## Product decisions
Barcode scanning, price tracking and a live recipe API were cut from v1 because they need external services and would have delayed testing the core loop. The grocery list moved into v1 once it was clear it was pure logic with no dependencies.
