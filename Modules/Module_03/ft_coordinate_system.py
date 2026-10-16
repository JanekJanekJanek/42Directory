import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            args = input("📍Enter new coordinates as floats in format"
                         " 'x,y,z': ").split(",")
            i = 0
            for arg in args:
                float(arg)
                i += 1
            if i == 3:
                return float(args[0]), float(args[1]), float(args[2])
            else:
                raise ValueError
        except ValueError:
            print("Invalid syntax")


def calc_distance(p0: tuple[float, float, float],
                  p1: tuple[float, float, float]) -> float:
    dist = round(math.sqrt((p0[0] - p1[0])**2 + (p1[1] - p0[1])**2 +
                           (p1[2] - p0[2])**2), 4)
    return dist


def main() -> None:
    print("=== Game Coordinate System ===\n")
    p0 = (0, 0, 0)
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist_to_center: float = calc_distance(p0, p1)
    print(f"Distance to center: {dist_to_center}")
    print("\nGet a second set of coordinates")
    p2 = get_player_pos()
    dist_coords = calc_distance(p1, p2)
    print(f"Distance between the 2 sets of coordinates: {dist_coords}")


if __name__ == "__main__":
    main()
