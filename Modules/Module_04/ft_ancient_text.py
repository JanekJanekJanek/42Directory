import sys


def main() -> None:
    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            print("=== Cyber Archives Recovery ===")
            io = open(file, "r")
            print(f"Accesing file '{file}'\n---\n")
            print(f"{io.read()}")
            print("---")
            print(f"File '{file}' closed.")
            io.close()
        except (FileNotFoundError, IsADirectoryError,
                PermissionError, NotADirectoryError) as e:
            print(f"Error opening file '{file}': {e}")
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
# /etc/shadow - restricted read access
