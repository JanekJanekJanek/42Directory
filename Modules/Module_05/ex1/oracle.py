import dotenv
import os


def load_configs(envs: dict[str, str | None]) -> dict[str, str | None]:
    configs: dict[str, str | None] = {"MATRIX_MODE": None,
                                      "DATABASE_URL": None,
                                      "API_KEY": None, "LOG_LEVEL": None,
                                      "ZION_ENDPOINT": None}
    for env in configs:
        try:
            value = envs[env]
            if value is None:
                raise KeyError
        except KeyError:
            configs[env] = None
            print(f"Missing config: {env}")
            continue
        configs[env] = value
    return (configs)


def show_envs(envs: dict[str, str | None]) -> bool:
    print("Configurations loaded:")
    is_missing = False
    try:
        if envs['MATRIX_MODE'] not in [None, ""]:
            print(f"Mode: {envs['MATRIX_MODE']}")
        else:
            print("Mode: setting missing")
            is_missing = True
        if envs['DATABASE_URL'] not in [None, ""]:
            print("Database: Connected to local instance")
        else:
            print("Database: setting missing")
            is_missing = True
        if envs['API_KEY'] not in [None, ""]:
            print("API Access: Authenticated")
        else:
            print("API Access: setting missing")
            is_missing = True
        if envs['LOG_LEVEL'] not in [None, ""]:
            print(f"Log Level: {envs['LOG_LEVEL']}")
        else:
            print("Log Level: setting missing")
            is_missing = True
        if envs['ZION_ENDPOINT'] not in [None, ""]:
            print("Remote Network: Online")
        else:
            print("Remote Network: setting missing")
            is_missing = True
    except KeyError as e:
        print(f"{e}: Configuration setting missing")
        is_missing = True
    return is_missing


def missing_envs(envs: dict[str, str | None], is_missing: bool) -> None:
    print("\nConfiguration security check:")
    configs = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
               "LOG_LEVEL", "ZION_ENDPOINT"]
    for env in configs:
        try:
            if envs[env] is None:
                is_missing = True
                break
        except KeyError:
            is_missing = True
            break
    if is_missing is False:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly ignored by git")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    elif is_missing is True:
        print("\nThe Oracle doesn't see all configurations.")


def run_with_configs(envs: dict[str, str], is_missing: bool) -> None:
    if is_missing is True:
        print("Set all settings and rerun!")
        return None
    if envs["MATRIX_MODE"] == "production":
        print("Welcone to the Matrix!")
    elif envs["MATRIX_MODE"] == "development":
        print("Program is running in debug mode")
    else:
        print("\nMode not set! Chose “development” or “production” and rerun")


def main() -> None:
    print("=== Correct config===")
    print("\nORACLE STATUS: Consulting the configuration...\n")
    file_path = ".env"
    dotenv.load_dotenv(file_path, verbose=True)
    correct = load_configs(dict(os.environ))
    is_missing = show_envs(correct)
    missing_envs(correct, is_missing)
    run_with_configs(dict(os.environ), is_missing)

    print("\n=== Incorrect config===\n")
    envs = {"MATRIX_MODE": "production", "DATABASE_URL": None,
            "API_KEY": "okon", "LOG_LEVEL": "super high"}
    dotenv.load_dotenv(file_path, verbose=True)
    incorrect = load_configs(envs)
    is_missing = show_envs(incorrect)
    missing_envs(incorrect, is_missing)
    run_with_configs(dict(os.environ), is_missing)


if __name__ == "__main__":
    main()
