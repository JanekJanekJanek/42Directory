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


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_names: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_names:
            water_plant(plant)
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
