class Plant:
    class Stats:
        def __init__(self, name: str) -> None:
            self._name = name
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def calls_counter(self, grow_calls: int, age_calls: int,
                          show_calls: int) -> None:
            self._grow_calls += grow_calls
            self._age_calls += age_calls
            self._show_calls += show_calls

        def show_stats(self) -> None:
            print(f"[statistics for {self._name}]")
            print(f"Stats: {self._grow_calls} grow, {self._age_calls}",
                  f"age, {self._show_calls} show")

    def __init__(self, name: str, s_height: float = 42.42, s_age: int = 42,
                 growth_rate: float = 4.2) -> None:
        self.name = name
        if s_height >= 0:
            self._s_height = s_height
        else:
            print("Height can't be negative! (default value set)")
        if s_age >= 0:
            self._s_age = s_age
        else:
            print("Age can't be negative! (default value set)")
        if growth_rate >= 0:
            self._growth_rate = growth_rate
        else:
            print("Growth rate can't be negative! (default value set)")
        self.stats = self.Stats(name)

    def show(self) -> None:
        print(f"{self.name}: {round(self._s_height, 1)}cm,",
              f"{self._s_age}", "days old")
        self.stats.calls_counter(0, 0, 1)

    def grow(self) -> None:
        self._s_height += self._growth_rate
        self.stats.calls_counter(1, 0, 0)

    def age(self) -> None:
        self._s_age += 1
        self.stats.calls_counter(0, 1, 0)

    def set_height(self, height: int) -> None:
        if height > 0:
            self._s_height = height
            print(f"Height updated: {self._s_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age > 0:
            self._s_age = age
            print(f"Age updated: {self._s_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._s_height

    def get_age(self) -> int:
        return self._s_age

    @staticmethod
    def is_year_or_more(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False

    @classmethod
    def anonymus(cls) -> 'Plant':
        return cls("Unknown plant", 0, 0, 0)


class Flower(Plant):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, color: str):
        super().__init__(name, s_height, s_age, growth_rate)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} hasn't bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self._shadow_calls = 0

        def shadow_counter(self, shadow_call: int) -> None:
            self._shadow_calls += shadow_call

        def show_stats(self) -> None:
            super().show_stats()
            print(f"{self._shadow_calls} shadow")

    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, s_height, s_age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._is_giving_shade = False
        self.stats: Tree.Stats = self.Stats(name)

    def produce_shade(self) -> None:
        if self._is_giving_shade is False:
            print(f"[asking the {self.name} to produce shade...]")
        self._is_giving_shade = True
        print(f"Tree {self.name} now produces a shade of ",
              f"{self._s_height}cm long and ",
              f"{self._trunk_diameter}cm wide.", sep="")
        self.stats.shadow_counter(1)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: float) -> None:
        super().__init__(name, s_height,
                         s_age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest_season: {self._harvest_season}")
        print(f"Nutritional_value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, s_height, s_age, growth_rate, color)
        self._seeds_num = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds_num = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds_num}")


def universal_stats(any_plant: Plant) -> None:
    any_plant.stats.show_stats()


def main() -> None:
    print("=== Garden statistics ===\n=== Check year-old")
    print("Is 30 days more than a year? ->",
          f"{Plant.is_year_or_more(30)}")
    print("Is 400 days more than a year? ->",
          f"{Plant.is_year_or_more(400)}")
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, 1.2, "Red")
    rose.show()
    rose.stats.show_stats()
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 1, 5.0)
    oak.show()
    oak.stats.show_stats()
    print("asking Oak to produce shadow")
    oak.produce_shade()
    oak.produce_shade()
    oak.stats.show_stats()
    print("\n=== Seed")
    sunfl = Seed("Sunflower", 80, 45, 1.5, "yellow")
    sunfl.show()
    print("[make sunflower grow, age and bloom]")
    for day in range(20):
        sunfl.age()
        sunfl.grow()
    sunfl.bloom()
    sunfl.show()
    sunfl.stats.show_stats()
    print("\n=== Anonymous")
    anon = Plant.anonymus()
    anon.show()
    print("\n=== Any plant")
    universal_stats(oak)
    universal_stats(sunfl)
    any_plant = Plant("Pythoneum", 4242, 74777777, 0)
    for day in range(222223):
        any_plant.age()
        any_plant.grow()
    any_plant.show()
    universal_stats(any_plant)


if __name__ == "__main__":
    main()
