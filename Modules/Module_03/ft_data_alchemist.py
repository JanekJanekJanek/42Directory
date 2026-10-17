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
