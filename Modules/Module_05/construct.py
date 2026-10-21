import os
import sys
import site


def main() -> None:
    if sys.prefix != sys.base_prefix:
        path = os.environ.get("VIRTUAL_ENV")
        venv_name = os.path.basename(path)
        curr_python = sys.executable
        packages = site.getsitepackages()[0]
        print("\nLABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {curr_python}", f"\nVirtual Environment: {venv_name}",
            f"\nEnvironment Path: {path}\n")
        print("SUCCESS: You are working in an isolated environment!",
                "\nSafe to install reagents without affecting the global system.")
        print(f"\nReagent installation path:\n{packages}")
    else:
        curr_python = os.environ.get("_")
        print("\nLABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {curr_python}")
        print("Virtual environment: undetected\n")
        print("WARNING: You are in the global environment!",
                "\nEvery reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:\npython3 -m venv lab_env\nsource",
            " lab_env/bin/activate # On Unix", "\nlab_env\\Scripts\\activate",
            "# On Windows\n Then run this program again")


if __name__ == "__main__":
    main()
