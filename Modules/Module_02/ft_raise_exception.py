def input_temperature(temp_str: str) -> int:
    t = int(temp_str)
    if t >= 0 and t <= 40:
        return t
    else:
        if t < 0:
            raise ValueError(f"{t}°C is too cold for plants (min 0°C)")
        else:
            raise ValueError(f"{t}°C is too hot for plants (max 40°C)")


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
    test_temperature("100")
    test_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
