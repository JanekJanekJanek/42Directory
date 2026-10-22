import importlib
import sys


def check_reagents(reagents: str) -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    reagents = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
    }

    missing_reagents = []
    installed_info = []

    for name, description in reagents.items():
        try:
            mod = importlib.import_module(name)
            version = getattr(mod, "__version__", "unknown")
            installed_info.append(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            missing_reagents.append(name)

    if missing_reagents:
        print(f"[FAIL] Missing required reagents: {', '.join(missing_reagents)}\n")
        print("To install missing reagents, run:")
        print("  pip:    pip install -r ex0/requirements.txt")
        print("  Poetry: poetry install\n")
        sys.exit(0)

    for info in installed_info:
        print(info)

    print(
        "\npip vs Poetry: requirements.txt declares what to install; pip resolves "
        "it at install time. pyproject.toml declares the same constraints, and "
        "Poetry pins the resolved versions in poetry.lock so every install is identical.\n"
    )
    print("All reagents present and accounted for.")


if __name__ == "__main__":
    reagents = {"pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "lib": "nonthing"}
    check_reagents(reagents)
