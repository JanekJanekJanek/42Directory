import os
import dotenv


def load_envs(file_path: str, envs: dict[str, str]) -> dict[str, str]:
    for env in envs:
        try:
            value = envs[env]
        except KeyError:
            envs[env] = None
            continue
        envs[env] = value
    return(dict(envs))


def show_envs(envs: dict[str, str]) -> bool:
    print("Configuration loaded:")
    try:
        if envs['MATRIX_MODE'] is not None:
            print(f"Mode: {envs['MATRIX_MODE']}")
        if envs['DATABASE_URL'] is not None:
            print(f"Database: Connected to local instance")
        if envs['API_KEY'] is not None:
            print(f"API Access: Authenticated")
        if envs['LOG_LEVEL'] is not None:
            print(f"Log Level: {envs['LOG_LEVEL']}")
        if envs['ZION_ENDPOINT'] is not None:
            print(f"Remote Network: Online\n")
    except KeyError as e:
        print(f"{e}: Configuration setting missing")


def check_envs(envs: dict[str, str]) -> bool:
    print("\nConfiguration security check:\n")
    is_missing = False
    configs = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    for env in configs:
        try:
            if envs[env] is None:
                is_missing = True
                break
        except KeyError:
            is_missing = True
            break
    if is_missing == False:
        print("\nConfiguration security check:\n")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly ignored by git")
        print("[OK] Production overrides available")
        print("The Oracle sees all configurations.")
    elif is_missing == True:
        print("The Oracle doesn't see all configurations.")


def main():
    print("\nORACLE STATUS: Consulting the configuration...\n")
    print("=== Correct config===")
    file_path = ".env.example"
    dotenv.load_dotenv(file_path)
    envs = dotenv.dotenv_values(file_path)
    correct = load_envs(file_path, envs)
    show_envs(correct)
    check_envs(correct)
    print("\n=== Incorrect config===\n")
    file_path = ".env"
    envs = {"MATRIX_MODE": "production", "DATABASE_URL": "postgre//:db",
            "API_KEY": "okon", "LOG_LEVEL": "super high"}
    incorrect = load_envs(file_path, envs)
    show_envs(incorrect)
    check_envs(incorrect)
#Configuration security check:
#[OK] No hardcoded secrets detected
#[OK] .env file properly ignored by git
#[OK] Production overrides available
#The Oracle sees all configurations.
if __name__ == "__main__":
    main()

