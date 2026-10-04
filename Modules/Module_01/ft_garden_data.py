class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def title(self):
        print("=== Garden Plant Registry ===")

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 20, 30)
    rose.height = rose.height + 5
    sunflower = Plant("Moonflower", 80, 45)
    sunflower.name = "Sunflower"
    cactus = Plant("Cactus", 15, 105)
    cactus.age += 15
    rose.title(), rose.show(), sunflower.show(), cactus.show()
