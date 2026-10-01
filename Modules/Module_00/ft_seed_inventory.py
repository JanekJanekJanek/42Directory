def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type
    if unit == "packets":
        print(f"{seed.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
