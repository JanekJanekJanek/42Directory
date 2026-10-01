def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def print_day(day: int) -> None:
        print("Day", day)
    for day in range(1, days + 1):
        print_day(day)
        day -= 1
    print("Harvest time!")
