from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eye-ball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if "INVALID" in validate_ingredients(ingredients):
        return f"spell NOT recorded: {spell_name} "\
                f"({validate_ingredients(ingredients)})"
    elif "VALID" in validate_ingredients(ingredients):
        return f"spell recorded: {spell_name} "\
                f"({validate_ingredients(ingredients)})"
    return "Not VALIDATED"
