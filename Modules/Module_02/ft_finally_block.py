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
