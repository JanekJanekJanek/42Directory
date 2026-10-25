def main() -> None:
    print("=== Kaboom 1 ===\n"
          "Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record\
        as spell_record
    print(spell_record("☄️ dark Vortex", "dark frogs void"))


if __name__ == "__main__":
    main()
