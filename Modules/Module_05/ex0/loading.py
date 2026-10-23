import importlib
import sys


def check_reagents(reagents: dict[str, str]) -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    missing_reagents = []
    for name, description in reagents.items():
        try:
            mod = importlib.import_module(name)
            version = getattr(mod, "__version__")
            print(f"[OK] {name} ({version}) - {description}")
        except AttributeError:
            if name in sys.stdlib_module_names:
                print(f"[OK]'{name}' is from stdlib"
                      " - doesn't require installing")
        except ImportError:
            missing_reagents.append(name)
    if missing_reagents:
        print("[FAIL] Missing required reagents:"
              f" {', '.join(missing_reagents)}\n")
        print("To install missing reagents, run:")
        print("  pip:    pip install -r ex0/requirements.txt")
        print("  Poetry: poetry install\n")
        sys.exit(0)
    print("\npip vs Poetry: requirements.txt declares what to install;"
          " pip resolves it at install time. pyproject.toml declares the"
          " same constraints, and Poetry pins the resolved versions in "
          "poetry.lock so every install is identical.\n")
    print("All reagents present and accounted for.")


if __name__ == "__main__":
    reagents = {"pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "os": "stdlib module, not third-party package"}
    check_reagents(reagents)
