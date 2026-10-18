import sys


def read_file() -> str | None:
    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            print(f"Accesing file '{file}'")
            io = open(file, "r")
            print("=== Cyber Archives Recovery & Preservation ===\n---\n")
            content = io.read()
            print(f"{content}")
            print("---")
            print(f"File '{file}' closed.\n")
            io.close()
            return content
        except (FileNotFoundError, IsADirectoryError,
                PermissionError, NotADirectoryError) as e:
            print(f"{sys.stderr.name} Error opening file '{file}': {e}",
                  file=sys.stderr)
            return None
    else:
        print("Usage: ft_stream_managment.py <file>")
    return None


def write_file(content: str) -> None:
    string = ""
    try:
        for char in content:
            if char == "\n":
                string += "#" + char
                continue
            else:
                string += char
        print("Transform data:\n---\n")
        print(f"{string}")
        print("\n---")
    except TypeError:
        return
    try:
        new_file = input("Enter new file name (or leave empty to skip): ")
        if new_file != "":
            print(f"Saving data to '{new_file}'")
            io = open(new_file, "w")
            io.write(string)
            print(f"Data saved in file '{new_file}'")
            io.close()
        else:
            print("Saving to file skipped")
    except (TypeError, IsADirectoryError,
            PermissionError, NotADirectoryError) as e:
        print(f"{sys.stderr.name} Error writing to file '{new_file}': {e}",
              file=sys.stderr)
        print("Data not saved")


def main() -> None:
    try:
        content = read_file()
        if content is not None:
            write_file(content)
    except (FileNotFoundError, IsADirectoryError,
            PermissionError, NotADirectoryError):
        pass


if __name__ == "__main__":
    main()
# /home/jziental/git_General_Repo/Modules/Module_04/Data_Vault_7
