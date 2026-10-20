def secure_archive(file: str, mode: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(file, mode) as check:
                read = check.read()
                return (True, read)
        elif mode == "w":
            with open(file, mode) as check:
                check = check.write(content)
                return (True, "Content successfully written to file")
        else:
            raise TypeError("Invalid mode parameter")
    except (FileNotFoundError, IsADirectoryError,
            PermissionError, NotADirectoryError, TypeError) as e:
        return (False, str(e))


def main() -> None:
    print("===Cyber Archives Security===\n")
    nonexist = "/not/existing/file"
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive(nonexist), "\n")
    inacces = "/etc/shadow"
    print("Using 'secure_archive' to read from"
          "an inaccessible nonexistent file:")
    print(secure_archive(inacces), "\n")
    print("Using 'secure_archive' to read from a regular file:")
    regular = "Data_Vault_7"
    print(secure_archive(regular), "\n")
    write = "Data_Vault_7++"
    content = secure_archive(regular)
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive(write, "w", content[1]), "\n")
    #print(secure_archive(write, "g", content[1]), "\n")


if __name__ == "__main__":
    main()
