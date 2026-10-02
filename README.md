# 42 exercises

## Export a module for Gemini Notebook

From this directory, run:

```powershell
python .\export_module.py Module_00
```

The combined file is written to `exports/Module_00.md`. Upload that one file
to Gemini Notebook.

For later modules, change only the module name:

```powershell
python .\export_module.py Module_01
python .\export_module.py Module_02
```

The exporter includes every `.py` file in the module, sorted by filename, and
skips `main.py` because it is the interactive test helper. Include it when
needed with:

```powershell
python .\export_module.py Module_00 --include-main
```
