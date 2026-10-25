from elements import create_fire
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold 🔗🔄🪙 :\n"
            f" brew '{create_air()}' and '{strength_potion()}'"
            f" mixed with '{create_fire()}'")
