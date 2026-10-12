import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    length = len(sys.argv)
    if length < 2:
        print("No arguments provided!")
    i = 1
    print(f"Arguments received: {length - 1}")
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {length}")


if __name__ == "__main__":
    main()
