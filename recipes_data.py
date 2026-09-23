"""
Recipe dataset for PantryMatch.

Each recipe lists its core ingredients in lowercase, singular form so they can
be matched against whatever the user says they have on hand. This is a small
hand-curated v1 dataset -- swappable later for a real recipe API (Spoonacular,
Edamam) once the matching logic is validated.
"""

RECIPES = [
    {
        "name": "Veggie Fried Rice",
        "tags": ["dinner", "quick", "vegetarian"],
        "time_minutes": 20,
        "ingredients": ["rice", "egg", "soy sauce", "frozen peas", "carrot", "garlic", "green onion"],
        "instructions": "Scramble egg, set aside. Saute garlic, carrot, peas. Add cold rice, "
                        "soy sauce, and egg back in. Top with green onion.",
    },
    {
        "name": "Pasta Aglio e Olio",
        "tags": ["dinner", "quick", "vegetarian"],
        "time_minutes": 15,
        "ingredients": ["pasta", "garlic", "olive oil", "red pepper flakes", "parmesan", "parsley"],
        "instructions": "Boil pasta. Saute sliced garlic in olive oil until golden, add chili "
                        "flakes. Toss with pasta, top with parmesan and parsley.",
    },
    {
        "name": "Black Bean Tacos",
        "tags": ["dinner", "quick", "vegetarian"],
        "time_minutes": 15,
        "ingredients": ["black beans", "tortilla", "onion", "cumin", "lime", "cheese", "cilantro"],
        "instructions": "Saute onion, add beans and cumin, mash slightly. Fill tortillas, top "
                        "with cheese, lime, and cilantro.",
    },
    {
        "name": "Chicken Stir Fry",
        "tags": ["dinner", "quick"],
        "time_minutes": 25,
        "ingredients": ["chicken breast", "soy sauce", "garlic", "ginger", "bell pepper", "broccoli", "rice"],
        "instructions": "Cube and cook chicken. Add garlic, ginger, vegetables. Toss in soy "
                        "sauce. Serve over rice.",
    },
    {
        "name": "Overnight Oats",
        "tags": ["breakfast", "quick", "vegetarian"],
        "time_minutes": 5,
        "ingredients": ["oats", "milk", "yogurt", "honey", "banana", "peanut butter"],
        "instructions": "Combine oats, milk, and yogurt in a jar. Refrigerate overnight. Top "
                        "with banana, honey, and peanut butter.",
    },
    {
        "name": "Veggie Omelet",
        "tags": ["breakfast", "quick", "vegetarian"],
        "time_minutes": 10,
        "ingredients": ["egg", "cheese", "bell pepper", "onion", "spinach", "butter"],
        "instructions": "Whisk eggs. Saute vegetables in butter, add eggs, fold in cheese once "
                        "set.",
    },
    {
        "name": "Lentil Soup",
        "tags": ["dinner", "vegetarian", "batch-cook"],
        "time_minutes": 40,
        "ingredients": ["lentils", "onion", "carrot", "celery", "garlic", "vegetable broth", "cumin"],
        "instructions": "Saute onion, carrot, celery, garlic. Add lentils, broth, and cumin. "
                        "Simmer 30 minutes.",
    },
    {
        "name": "Caprese Salad",
        "tags": ["lunch", "quick", "vegetarian", "no-cook"],
        "time_minutes": 5,
        "ingredients": ["tomato", "mozzarella", "basil", "olive oil", "balsamic vinegar"],
        "instructions": "Slice tomato and mozzarella, layer with basil, drizzle with oil and "
                        "vinegar.",
    },
    {
        "name": "Turkey Chili",
        "tags": ["dinner", "batch-cook"],
        "time_minutes": 35,
        "ingredients": ["ground turkey", "black beans", "tomato", "onion", "garlic", "chili powder", "cumin"],
        "instructions": "Brown turkey with onion and garlic. Add tomato, beans, and spices. "
                        "Simmer 25 minutes.",
    },
    {
        "name": "Greek Yogurt Parfait",
        "tags": ["breakfast", "quick", "vegetarian", "no-cook"],
        "time_minutes": 5,
        "ingredients": ["yogurt", "granola", "honey", "berries"],
        "instructions": "Layer yogurt, granola, and berries. Drizzle with honey.",
    },
    {
        "name": "Shakshuka",
        "tags": ["breakfast", "dinner", "vegetarian"],
        "time_minutes": 25,
        "ingredients": ["egg", "tomato", "onion", "bell pepper", "garlic", "cumin", "paprika"],
        "instructions": "Saute onion, pepper, garlic. Add crushed tomato and spices, simmer. "
                        "Crack eggs into sauce, cover until set.",
    },
    {
        "name": "Peanut Noodles",
        "tags": ["dinner", "quick", "vegetarian"],
        "time_minutes": 15,
        "ingredients": ["noodles", "peanut butter", "soy sauce", "garlic", "lime", "carrot", "green onion"],
        "instructions": "Whisk peanut butter, soy sauce, garlic, and lime into a sauce. Toss "
                        "with cooked noodles and shredded carrot.",
    },
    {
        "name": "Baked Salmon & Veggies",
        "tags": ["dinner"],
        "time_minutes": 25,
        "ingredients": ["salmon", "broccoli", "lemon", "olive oil", "garlic"],
        "instructions": "Toss broccoli in oil and garlic. Bake with salmon at 400F for 15-18 "
                        "min. Finish with lemon.",
    },
    {
        "name": "Quesadillas",
        "tags": ["lunch", "dinner", "quick", "vegetarian"],
        "time_minutes": 10,
        "ingredients": ["tortilla", "cheese", "onion", "bell pepper", "black beans"],
        "instructions": "Fill tortilla with cheese and sauteed vegetables, fold, and crisp in a "
                        "dry pan on both sides.",
    },
    {
        "name": "Banana Pancakes",
        "tags": ["breakfast", "vegetarian"],
        "time_minutes": 15,
        "ingredients": ["flour", "banana", "egg", "milk", "butter", "honey"],
        "instructions": "Mash banana into batter of flour, egg, and milk. Cook on a buttered "
                        "pan, top with honey.",
    },
]

ALL_INGREDIENTS = sorted({ing for r in RECIPES for ing in r["ingredients"]})
