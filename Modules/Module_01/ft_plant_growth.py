class Plant:
    def __init__(self, name : str, height: float, age_days: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate
    def show(self) -> None:
        print("COPY FROM PREVIOUS")
    def grow(self) -> None:
        self.height += self.growth_rate
    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30, 1.2)
    print("=== Garden Plant Growth ===")
    print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.age_days} days old")
    for day in range (1, 8):
        print(f"=== Day {day} ===")
        print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.age_days} days old")
        rose.grow()
        rose.age()
