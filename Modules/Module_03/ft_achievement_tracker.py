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
    print(f"\nCommon achivements: {common_achivements}")
    i = 0
    for player in players:
        others:  set[str] = set()
        for j in range(len(players)):
            if i != j:
                others = others.union(achivs[j])
        unique = achivs[i].difference(others)
        print(f"Only {player} has: {unique}")
        i += 1
    i = 0
    for player in players:
        missing = distinict_achivements.difference(achivs[i])
        print(f"{player} is missing: {missing}")
        i += 1


if __name__ == "__main__":
    main()
