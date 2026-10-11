def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    try:
        print(f"Input data is '{temp_str}'")
        print(f"Temperature is now {input_temperature(temp_str)}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
