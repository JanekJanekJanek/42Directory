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
