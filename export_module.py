#!/usr/bin/env python3
"""Export one 42 module's Python exercises into a Gemini-friendly Markdown file."""

from argparse import ArgumentParser
from pathlib import Path


def export_module(module_name: str, include_main: bool = False) -> Path:
    """Write all Python files in a module to one Markdown file."""
    root = Path(__file__).resolve().parent
    module_dir = root / "Modules" / module_name
    if not module_dir.is_dir():
        raise FileNotFoundError(f"Module directory not found: {module_dir}")

    files = sorted(module_dir.glob("*.py"))
    if not include_main:
        files = [path for path in files if path.name != "main.py"]
    if not files:
        raise FileNotFoundError(f"No exercise files found in {module_dir}")

    output_dir = root / "exports"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"my_{module_name.capitalize()}.md"

    with output_path.open("w", encoding="utf-8", newline="\n") as output:
        output.write(f"# {module_name} exercises\n\n")
        output.write(
            "This file contains the Python exercise files from "
            f"`Modules/{module_name}`.\n\n"
        )
        for path in files:
            contents = path.read_text(encoding="utf-8")
            output.write(f"## `{path.name}`\n\n```python\n")
            output.write(contents)
            if not contents.endswith("\n"):
                output.write("\n")
            output.write("```\n\n")

    return output_path


def main() -> None:
    parser = ArgumentParser(
        description="Combine a module's Python exercises into one Markdown file."
    )
    parser.add_argument(
        "module",
        help="Module directory name, for example Module_00 or Module_01",
    )
    parser.add_argument(
        "--include-main",
        action="store_true",
        help="Also include the module's main.py test helper",
    )
    args = parser.parse_args()

    output_path = export_module(args.module, args.include_main)
    print(f"Exported {args.module} to {output_path}")


if __name__ == "__main__":
    main()
