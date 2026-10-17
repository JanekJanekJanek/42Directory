# Module_03 exercises

This file contains the Python exercise files from `Modules/Module_03`.

## `ft_achievement_tracker.py`

```python
import random


def gen_player_achievements() -> set[str]:
    achievements_list = [
        "Warm-Up Act", "Someone's Awakening", "Sharpshooter", "Downbeat",
        "7/4 Time", "Shocking Developments", "Fortissimo!", "The King of Evil",
        "Hasters Gonna Haste", "Spearmaster", "Masquerade", "Gladiator",
        "Hale and Hearty", "THIEF", "Lonely Digging", "Falling Down",
        "Hot Feet", "Master Angler", "Major Key", "Virtuoso", "Classic Mode",
        # "Capital Gains", "Flam", "Brainiac", "Expansive Repertoire",
        # "Eight Sharps", "The Eye of Gohma", "'Splodenspiel", "Cool Riffs",
        # "Hot Beats", "Sight Reading", "Allegro",
        # "What Doesn't Kill You Makes You Conga", "The Lowest of the Low",
        # "Friendly Fire", "Lightning Strikes Twice", "Minimalism",
        # "Flawless Performance", "Bee Bop", "Unarmed and Dangerous",
        # "Turn It Down", "Freeform Jazz", "Prestissimo", "No Steps Wasted",
        # "Come Reign or Shrine", "16-Bit Party People", "Shortcutter",
        "Necro-Mastery"]
    num = random.randint(len(achievements_list) // 4, len(achievements_list))
    return set(random.choices(achievements_list, k=num))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print(".,ø¤°`°¤ø,.,ø¤°`°¤ø,.,ø¤°`°¤ø,.\n")
    players = ["Link", "Zelda", "Daruk", "Urbosa"]
    achivs = []
    i = 0
    for player in players:
        achivs.append(gen_player_achievements())
        print(f"Player {player}: {achivs[i]}")
        i += 1
    distinict_achivements = achivs[0] | achivs[1] | achivs[2] | achivs[3]
    print(f"\nAll distinct achivements: {distinict_achivements}")
    common_achivements = achivs[0] & achivs[1] & achivs[2] & achivs[3]
    print(f"\nCommon achivements: {common_achivements}\n")
    i = 0
    for player in players:
        others:  set[str] = set()
        for j in range(len(players)):
            if i != j:
                others = others.union(achivs[j])
        unique = achivs[i].difference(others)
        print(f"Only {player} has: {unique}")
        i += 1
    print()
    i = 0
    for player in players:
        missing = distinict_achivements.difference(achivs[i])
        print(f"{player} is missing: {missing}")
        i += 1


if __name__ == "__main__":
    main()
```

## `ft_command_quest.py`

```python
import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    length = len(sys.argv)
    if length < 2:
        print("No arguments provided!")
    i = 1
    print(f"Arguments received: {length - 1}")
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {length}")


if __name__ == "__main__":
    main()
```

## `ft_coordinate_system.py`

```python
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            args = input("📍Enter new coordinates as floats in format"
                         " 'x,y,z': ").split(",")
            i = 0
            for arg in args:
                float(arg)
                i += 1
            if i == 3:
                return float(args[0]), float(args[1]), float(args[2])
            else:
                raise ValueError
        except ValueError:
            print("Invalid syntax")


def calc_distance(p0: tuple[float, float, float],
                  p1: tuple[float, float, float]) -> float:
    dist = round(math.sqrt((p0[0] - p1[0])**2 + (p1[1] - p0[1])**2 +
                           (p1[2] - p0[2])**2), 4)
    return dist


def main() -> None:
    print("=== Game Coordinate System ===\n")
    p0 = (0, 0, 0)
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist_to_center: float = calc_distance(p0, p1)
    print(f"Distance to center: {dist_to_center}")
    print("\nGet a second set of coordinates")
    p2 = get_player_pos()
    dist_coords = calc_distance(p1, p2)
    print(f"Distance between the 2 sets of coordinates: {dist_coords}")


if __name__ == "__main__":
    main()
```

## `ft_data_alchemist.py`

```python
import random


def main() -> None:
    players = ["Geralt", "yennefer", "Triss", "ciri", "Astarion",
               "shadowheart", "GALE", "karlach", "Lae'zel", "dandelion"]

    all_names = [name.capitalize() for name in players]
    cap_names = [name for name in players if name == name.capitalize()]
    scores = {name: random.randint(0, 10) for name in all_names}
    print("=== Game Data Alchemist🧪 ===\n")
    print(f"📜 Initial list of players: {players}")
    print(f"🔄 New list with all names capitalized: {all_names}")
    print(f"🔄 New list of capitalized names only: {cap_names}")
    print(f"\n📊 Score dict: {scores}")
    if len(scores) > 0:
        average = round(sum(scores.values()) / len(scores), 2)
        print(f"⚖️  Score average is {average}")
    else:
        print("⚖️ Score average is 0.00")
    highscores = {name: scores[name] for name in scores
                  if scores[name] > average}
    print(f"⭐ High scores: {highscores}")


if __name__ == "__main__":
    main()
```

## `ft_data_stream.py`

```python
import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["Bob", "Dylan", "Alice", "Charlie"]
    actions = ["eat", "code", "sleep", "debug"]
    event = (random.choice(players), random.choice(actions))
    yield event


def consume_event(events: list[tuple[str, str]]) -> \
        typing.Generator[list[tuple[str, str]], None, None]:
    rnd = random.randint(0, len(events) - 1)
    print(f"Got event from list: {events[rnd]}")
    events.pop(rnd)
    yield events


def main() -> None:
    for i in range(1, 1000 + 1):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    actions_log = []
    for i in range(10):
        actions_log.append((next(gen_event())))
    print(f"\nBuilt list of 10 events:\n{actions_log}\n")
    while len(actions_log) > 0:
        remaining = next(consume_event(actions_log))
        print(f"Remains in list {remaining}")


if __name__ == "__main__":
    main()
```

## `ft_inventory_system.py`

```python
import sys


class InventoryError(Exception):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)


class RedundantError(InventoryError):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = dict()
    for arg in sys.argv[1:]:
        try:
            pair = arg.split(":")
            if len(pair) == 2:
                if pair[0] in inventory.keys():
                    raise RedundantError(f"🚫 Redundant item '{pair[0]}'"
                                         " - discarding")
                elif int(pair[1]) > 0:
                    inventory.update({pair[0]: int(pair[1])})
                else:
                    raise InventoryError(f"🚫 Error - invalid quantity"
                                         f" '{pair[1]}'")
            else:
                raise InventoryError(f"🚫 Error - invalid parameter '{arg}'")
        except InventoryError as e:
            print(f"{e}")
        except RedundantError as e:
            print(f"{e}")
        except ValueError as e:
            print(f"🚫 Quantity error for '{pair[0]}': {e}")
    print(f"🎒 Got inventory: {inventory}")
    print(f"📋 Item list: {list(inventory.keys())}")
    total_quantity = sum(inventory.values())
    print(f"📋 Total quantity of the {len(inventory)} items:"
          f" {total_quantity}\n")
    for item in inventory:
        proportion = round(inventory[item] / total_quantity * 100, 1)
        print(f"➤ Item {item} represents {proportion}%")
    keys = list(inventory.keys())
    try:
        min_key = keys[0]
        max_key = keys[0]
        min_val = inventory[min_key]
        max_val = inventory[max_key]
        for key in keys:
            if inventory[min_key] > inventory[key]:
                min_key = key
                min_val = inventory[key]
            if inventory[max_key] < inventory[key]:
                max_key = key
                max_val = inventory[key]
    except IndexError:
        min_key = None
        max_key = None
        min_val = 0
        max_val = 0
    print(f"\n📈 Item most abundant: {max_key} with quantity {max_val}")
    print(f"🤏 Item least abundant: {min_key} with quantity {min_val}\n")
    inventory.update({"magic_item": 42})
    print(f"🎉 Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
```

## `ft_score_analytics.py`

```python
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    length = len(sys.argv)
    if length < 2:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = list()
        for arg in sys.argv[1:]:
            try:
                num = int(arg)
                scores.append(num)
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(scores) == 0:
            print("No scores provided. "
                  "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            print(rf"""
                \_\     /_/        \/_/         /_/      \/_/   \_\     /_/
                .-.  \.-./  .-.   .-./  .-.   .-./  .-.   .-\   .-.  \.-./  .-.
            //-\\_//-\\_//-\\_//-\\_//-\\_//-\\_// \\_//-\\_//-\\_//-\\_//-\\
            __(   '-'   '-'\  '-'   '-'  /'-'   '-'\__'-'   '-'__/'-'   '-'\__
            /_/))            \__       __/\          \_\       /_/           \_
        ___\_//
        /_/  ((        Scores processed: {scores}
            )) __
        __   // /_/     Total players: {len(scores)}
        \_\_((_/___
            ))  \_     Total score: {sum(scores)}
            \\
            )) _        Average score: {sum(scores) / len(scores)}
        __   // /_/
        \_\_((         High score: {max(scores)}
            \\
            )) _        Low score: {min(scores)}
        __   // /_/
        \_\_((_/___    Score range: {max(scores) - min(scores)}
            ))  \_\                __                    __
            \\     __       __     \_\  __          __   \_\  __   __       __
        __  ))    \_\     /_/        \/_/         /_/      \/_/   \_\     /_/
        \_\_((   .-.  \.-./  .-.   .-./  .-.   .-./  .-.   .-\   .-.  \.-./  .-
            \\_//-\\_//-\\_//-\\_//-\\_//-\\_//-\\_// \\_//-\\_//-\\_//-\\_//-\
                'dc\__'-'   '-'\  '-'   '-'  /'-'   '-'\__'-'   '-'__/'-'   '-'
            """)


if __name__ == "__main__":
    main()
```

