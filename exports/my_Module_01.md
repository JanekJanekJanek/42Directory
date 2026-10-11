# Module_01 exercises

This file contains the Python exercise files from `Modules/Module_01`.

## `ft_garden_analytics.py`

```python
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
```

## `ft_garden_data.py`

```python
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
```

## `ft_garden_intro.py`

```python
#!/usr/bin/env python3
def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    name = "Rose"
    height = 25
    age = 30
    print(f"Plant: {name}", f"Height: {height}cm", f"Age: {age}\
           days\n", sep="\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
```

## `ft_garden_security.py`

```python
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
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"Current state: {self.name}: {round(self._s_height, 1)}cm",
              f"{self._s_age}", "days old")

    def grow(self) -> None:
        self._s_height += self._growth_rate

    def age(self) -> None:
        self._s_age += 1

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

    def get_age(self) -> float:
        return self._s_age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10, 1.2)
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-42)
    rose.set_age(-42)
    print("")
    rose.show()
```

## `ft_plant_factory.py`

```python
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
```

## `ft_plant_growth.py`

```python
class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
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
```

## `ft_plant_types.py`

```python
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

    def get_age(self) -> float:
        return self._s_age


class Flower(Plant):
    def __init__(self, name: str, s_height: float, s_age: int,
                 growth_rate: float, color: str):
        super().__init__(name, s_height, s_age, growth_rate)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        if self._has_bloomed is False:
            print(f"[asking the {self.name} to bloom...]")
        self._has_bloomed = True

    def show(self) -> None:
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

    def produce_shade(self) -> None:
        if self._is_giving_shade is False:
            print(f"[asking the {self.name} to produce shade...]")
        self._is_giving_shade = True
        print(f"Tree {self.name} now produces a shade of ",
              f"{self._s_height}cm long and ",
              f"{self._trunk_diameter}cm wide.", sep="")

    def show(self) -> None:
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


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n===Flower")
    rose = Flower("Rose", 15, 10, 1.2, "Red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200, 10, 1.2, 5)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April", 0)
    tomato.show()
    days = 20
    for day in range(1, days + 1):
        tomato.grow()
        tomato.age()
        if day == 20:
            print(f"[make {tomato.name} grow and age for {days} days]")
    tomato.show()
```

