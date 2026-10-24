from alchemy.potions import healing_potion, strength_potion

def main() -> None:
    print("=== Distillation 0 ===\nDirect access to alchemy/potions.py")
    print(f"🥤 brewing health potion... {healing_potion()}")
    print(f"🥣 brewing strength potion... {strength_potion()}")


if __name__ == "__main__":
    main()
