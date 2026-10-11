class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self._message = message
        super().__init__(self._message)

    def __str__(self) -> str:
        return f"Caught {self.__class__.__name__}: {self._message}"


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


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
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"{e}")
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print(f"{e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
