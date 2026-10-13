import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            arg = input("Enter new coordinates as floats in format 'x,y,z': ")
            args = arg.split(",")
            coords = ()
            for arg in args:
                coord = float(arg)
                coords += (coord,)
            if len(coords) == 3:
                return coords
            else:
                raise ValueError
        except ValueError:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===")
    p0 = (0, 0, 0)
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist: float = round(math.sqrt((p0[0] - p1[0])**2 + (p1[1] - p0[0])**2 +
                        (p1[2] - p0[2])**2), 4)
    print(f"Distance to center: {dist}")


if __name__ == "__main__":
    main()
