class Plant:
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float) -> None:
        self.name = name
        if s_height > 0:
            self._s_height = s_height
        else:
            print("Height can't be negative! (default value set)")
            self._s_height = 42.42
        if s_age > 0:
            self._s_age = s_age
        else:
            print("Age can't be negative! (default value set)")
            self._s_age = 42
        if growth_rate > 0:
            self._growth_rate = growth_rate
        else:
            print("Growth rate can't be negative! (default value set)")
            self._growth_rate = 4.2

    def show(self) -> None:
        print(f"{self.name}: {round(self._s_height, 1)}cm,",
              f"{self._s_age}", "days old")

    def grow(self) -> None:
        self._s_height += self._growth_rate

    def age(self) -> None:
        self._s_age += 1

    def set_height(self, height: int):
        if height > 0:
            self._s_height = height
            print(f"Height updated: {self._s_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int):
        if age > 0:
            self._s_age = age
            print(f"Age updated: {self._s_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self):
        return self._s_height

    def get_age(self):
        return self._s_age

    @staticmethod
    def is_year_or_more(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False



class Flower(Plant):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, color: str):
        super().__init__(name, s_height, s_age, growth_rate)
        self._color = color
        self._has_bloomed = False

    def bloom(self):
        if self._has_bloomed is False:
            print(f"[asking the {self.name} to bloom...]")
        self._has_bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} hasn't bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, trunk_diameter: float):
        super().__init__(name, s_height, s_age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._is_giving_shade = False

    def produce_shade(self):
        if self._is_giving_shade is False:
            print(f"[asking the {self.name} to produce shade...]")
        self._is_giving_shade = True
        print(f"Tree {self.name} now produces a shade of ",
              f"{self._s_height}cm long and ",
              f"{self._trunk_diameter}cm wide.", sep="")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: float):
        super().__init__(name, s_height,
                         s_age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest_season: {self._harvest_season}")
        print(f"Nutritional_value: {self._nutritional_value}")

    def grow(self):
        super().grow()
        self._nutritional_value += 0.5

    def age(self):
        super().age()
        self._nutritional_value += 0.5


if __name__ == "__main__":
    print("=== Garden statistics ===\n=== Check year-old")
    print("Is 30 days more than a year? ->"
          ,f"{Plant.is_year_or_more(30)}")
    print("Is 400 days more than a year? ->"
          ,f"{Plant.is_year_or_more(400)}")
