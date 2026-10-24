import alchemy


def main() -> None:
    try:
        print("🌬️ ", alchemy.create_air())
        print(alchemy.create_earth())
    except AttributeError as e:
        print(f"🤯 Alembic broken! {e}")


if __name__ == "__main__":
    main()
