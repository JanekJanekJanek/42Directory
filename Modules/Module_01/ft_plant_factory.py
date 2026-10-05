class Plant:
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.s_height = s_height
        self.s_age = s_age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.s_height, 1)}cm, {self.s_age}",
              "days old")

    def grow(self) -> None:
        self.s_height += self.growth_rate

    def age(self) -> None:
        self.s_age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30, 1.2)
    oak = Plant("Oak", 200, 365, 0.1)
    cactus = Plant("Cactus", 5, 90, 0.5)
    sunflower = Plant("Sunflower", 80, 45, 3)
    fern = Plant("Fern", 15, 120, 0.7)
    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
