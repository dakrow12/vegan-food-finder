# server/tools/substitutions.py
SUBS = {
    "egg": [
        {"name": "Ground flax + water", "ratio": "1 tbsp + 3 tbsp water per egg", "best_for": ["pancakes","quick breads"], "notes":"Slightly nutty taste"},
        {"name": "Applesauce", "ratio": "1/4 cup per egg", "best_for": ["cakes","pancakes"], "notes":"Moist crumb; add 1/4 tsp baking powder"},
    ],
    "buttermilk": [
        {"name": "Plant milk + acid", "ratio": "1 cup soy/oat milk + 1 tbsp lemon juice", "best_for": ["pancakes","quick breads"], "notes":"Let sit 5 minutes"},
    ],
    "gelatin": [
        {"name": "Agar-agar", "ratio": "1 tsp powdered agar per 1 tsp gelatin", "best_for": ["gels"], "notes":"Needs a brief simmer to activate"},
    ],
}

def find_substitutions(ingredient: str):
    key = ingredient.strip().lower()
    return SUBS.get(key, [])
