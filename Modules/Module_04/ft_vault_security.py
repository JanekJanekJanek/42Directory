def secure_archive(file: str) -> tuple[bool, str]:
    try:
        check_read = open(file, "r")
        return (True, check_read.read())
    except (FileNotFoundError, IsADirectoryError,
                    PermissionError, NotADirectoryError) as e:
        return (False, str(e))

def main() -> None:
    print("===Cyber Archives Security===\n")
    nonexist = "/not/existing/file"
    print(secure_archive(nonexist))
    inacces = "/etc/shadow"
    print(secure_archive(inacces))
    regular = "Data_Vault_7"
    print(secure_archive(regular))


if __name__ == "__main__":
    main()
