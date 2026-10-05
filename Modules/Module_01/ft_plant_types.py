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


class Flower(Plant):
    pass

class Tree(Plant):
    pass

class Vegetable(Plant):
    pass


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
