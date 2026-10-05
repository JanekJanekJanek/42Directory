class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm,",
              f"{self.age_days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
