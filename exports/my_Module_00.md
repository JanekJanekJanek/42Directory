# Module_00 exercises

This file contains the Python exercise files from `Modules/Module_00`.

## `ft_count_harvest_iterative.py`

```python
def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print("Day", day)
    print("Harvest time!")
```

## `ft_count_harvest_recursive.py`

```python
def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def print_day(day: int) -> None:
        print("Day", day)
    for day in range(1, days + 1):
        print_day(day)
        day -= 1
    print("Harvest time!")
```

## `ft_garden_name.py`

```python
def ft_garden_name() -> None:
    garden = input("Enter garden name: ")
    print(f"Garden: {garden}")
    print("Status: Growing well!")
```

## `ft_harvest_total.py`

```python
def ft_harvest_total() -> None:
    d_one = input("Day 1 harvest: ")
    d_two = input("Day 2 harvest: ")
    d_three = input("Day 3 harvest: ")
    print(f"Total harvest: {int(d_one) + int(d_two) + int(d_three)}")
```

## `ft_hello_garden.py`

```python
def ft_hello_garden() -> None:
    print("Hello, Garden Community!")
```

## `ft_plant_age.py`

```python
def ft_plant_age() -> None:
    age = input("Enter plant age in days: ")
    if (int(age) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
```

## `ft_plot_area.py`

```python
def ft_plot_area() -> None:
    len = input("Enter length: ")
    width = input("Enter width: ")
    area = int(len) * int(width)
    print(f"Plot area: {area}")
```

## `ft_seed_inventory.py`

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type
    if unit == "packets":
        print(f"{seed.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
```

## `ft_water_reminder.py`

```python
def ft_water_reminder() -> None:
    days = input("Days since last watering:")
    if (int(days) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
```

## `main.py`

```python
#!/usr/bin/env python3

"""
Helper file for Growing Code.

This file helps you test your exercises easily.
Just run: python3 main.py

How it works:
1. It tries to import your exercise files (like ft_plot_area.py)
2. It calls your functions to test them
3. If there's an error, it tells you what went wrong

Make sure your exercise files are in the same folder as this main.py file!
"""


def test_ft_exercise(exercise_file_name):
    """
    This function tries to run one of your exercises.

    For example: test_ft_exercise("ft_plot_area") will:
    - Look for a file called ft_plot_area.py
    - Import it
    - Call the function ft_plot_area() inside it
    """
    print(f"\n=== Testing {exercise_file_name} ===")

    try:
        # Import your exercise file
        # This is like doing: import ft_plot_area
        import sys
        sys.path.append(".")
        ft_module = __import__(exercise_file_name)

        # Get the function from your file
        # This is like doing: ft_plot_area.ft_plot_area
        ft_function = getattr(ft_module, exercise_file_name)

        # Special handling for ft_seed_inventory (Exercise 7)
        # This function takes parameters, unlike the others
        if exercise_file_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            # Test with packets
            ft_function("tomato", 15, "packets")
            # Test with grams
            ft_function("carrot", 8, "grams")
            # Test with area
            ft_function("lettuce", 12, "area")
            # Test with unknown unit
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            # Run your function normally (no parameters)
            ft_function()

    except ImportError:
        print(f"❌ Could not find {exercise_file_name}.py")
        print(
            """   Make sure your file exists and is in the same
            folder as main.py"""
        )

    except AttributeError:
        print(f"❌ Could not find function {exercise_file_name}() in your file")
        print(f"   Make sure you have: def {exercise_file_name}():")

    except TypeError as error:
        msg = str(error)
        print(f"❌ Type error: {error}")
        if exercise_file_name == "ft_seed_inventory":
            if "missing" in msg and "required positional argument" in msg:
                print(
                    """   For exercise 7, make sure your
                    function takes parameters:"""
                )
                print(
                    f"   def {exercise_file_name}"
                    "(seed_type: str, quantity: int, unit: str) -> None:"
                )
        else:
            print("   Your function should not take any parameters")

    except Exception as error:
        print(f"❌ Error running your function: {error}")
        print("   Check your code for syntax errors")


def main():
    """Run main function - this runs when you execute: python3 main.py ."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.")
    print("\nWhich exercise would you like to test?")
    print()
    print("0 - ft_hello_garden     (Say hello to the garden community)")
    print("1 - ft_garden_name      (Display garden name)")
    print("2 - ft_plot_area        (Calculate garden plot area)")
    print("3 - ft_harvest_total    (Add up harvest weights)")
    print("4 - ft_plant_age        (Check if plant is ready)")
    print("5 - ft_water_reminder   (Check if plants need water)")
    print("6 - ft_count_harvest    (Count days to harvest)")
    print("7 - ft_seed_inventory   (Seed inventory with type hints)")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    # Test the exercise based on user choice
    if choice == "0":
        test_ft_exercise("ft_hello_garden")
    elif choice == "1":
        test_ft_exercise("ft_garden_name")
    elif choice == "2":
        test_ft_exercise("ft_plot_area")
    elif choice == "3":
        test_ft_exercise("ft_harvest_total")
    elif choice == "4":
        test_ft_exercise("ft_plant_age")
    elif choice == "5":
        test_ft_exercise("ft_water_reminder")
    elif choice == "6":
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
    elif choice == "7":
        test_ft_exercise("ft_seed_inventory")
    elif choice == "a":
        # Test all exercises one by one
        test_ft_exercise("ft_hello_garden")
        test_ft_exercise("ft_garden_name")
        test_ft_exercise("ft_plot_area")
        test_ft_exercise("ft_harvest_total")
        test_ft_exercise("ft_plant_age")
        test_ft_exercise("ft_water_reminder")
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
        test_ft_exercise("ft_seed_inventory")
    else:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, 7, or a")


# This line means: "If someone runs this file directly, call main()"
# You don't need to understand this yet, just know it makes the program start
if __name__ == "__main__":
    main()
```

