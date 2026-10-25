from .dark_spellbook import dark_spell_allowed_ingredients\
    as allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for ingredient in ingredients.split():
        if ingredient.casefold() in allowed_ingredients():
            return ingredients + " VALID"
    return ingredients + " INVALID"
