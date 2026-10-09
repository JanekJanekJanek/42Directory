class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    rose = Plant("Rose", 20, 30)
    rose.height = rose.height + 5
    sunflower = Plant("Moonflower", 80, 45)
    sunflower.name = "Sunflower"
    cactus = Plant("Cactus", 15, 105)
    cactus.age += 15
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
