# Module_02 exercises

This file contains the Python exercise files from `Modules/Module_02`.

## `ft_custom_errors.py`

```python
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self._message = message
        super().__init__(self._message)

    def __str__(self) -> str:
        return f"Caught {self.__class__.__name__}: {self._message}"


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self._message = message
        super().__init__(self._message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self._message = message
        super().__init__(self._message)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"{e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"{e}")
    print("\nTesting catching all garden errors...")
    errors = [GardenError("The tomato plant is wilting!"),
              GardenError("Not enough water in the tank!"),
              GardenError(), WaterError(), PlantError()]
    for err in errors:
        try:
            raise err
        except err.__class__ as err_messaga:
            print(f"{err_messaga}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
```

## `ft_different_errors.py`

```python
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
```

## `ft_finally_block.py`

```python
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self._message = message
        super().__init__(self._message)

    def __str__(self) -> str:
        return f"Caught {self.__class__.__name__}: {self._message}"


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self._message = message
        super().__init__(self._message)


def water_plant(plant_name: list[str]) -> None:
    for plant in plant_name:
        if plant == plant.capitalize():
            print(f"Watering {plant}: [OK]")
        else:
            raise PlantError(f"Invalid plant name to water: {plant}")


def test_watering_system(plant_name: list[str]) -> None:
    print("Opening watering system")
    try:
        water_plant(plant_name)
    except Exception as error:
        print(f"{error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    veggies = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(veggies)
    print("\nTesting invalid plants...")
    veggies = ["Tomato", "lettuce"]
    test_watering_system(veggies)
    print("\nCleanup always happens, even with errors! :}")


if __name__ == "__main__":
    main()
```

## `ft_first_exception.py`

```python
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
```

## `ft_raise_exception.py`

```python
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
```

