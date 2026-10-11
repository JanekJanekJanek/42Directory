def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        int("abc")
        return 0
    if operation_number == 1:
        42 / 0
        return 0
    if operation_number == 2:
        open("non/existen/file")
        return 0
    if operation_number == 3:
        "42" + 42
        return 0
    return 0


def test_error_types(operation_number: int) -> None:
    try:
        print(f"Testing operation {operation_number}...")
        garden_operations(operation_number)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: error {e}")
    else:
        print("Operation completed successfully")


def main() -> None:
    print("=== Garden Temperature ===")
    for e_num in range(5):
        test_error_types(e_num)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
