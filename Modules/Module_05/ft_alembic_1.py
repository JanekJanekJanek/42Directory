import alchemy


def main() -> None:
    try:
        print("===Alembic 1===")
        print("Accessing the alchemy module using 'import alchemy'")
        print("Testing create_air: 🌬️ ", alchemy.create_air())
        print(alchemy.create_earth())
    except AttributeError as e:
        print(f"...not all functions can be reached: 🤯 Alembic broken! {e}")


if __name__ == "__main__":
    main()
