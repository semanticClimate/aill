# aill

Prototype for the OKFN/ClimateAcademy/SemanticClimate AILL project. Style and layout follow [amilib](https://github.com/petermr/amilib) and [encyclopedia](https://github.com/semanticClimate/encyclopedia).

**Date:** 2025-02-28

## Layout

- **`aill/`** – Python package (code)
- **`docs/`** – Documentation
- **`temp/`** – Temporary/output files (not committed; see amilib style guide)
- **`test/`** – Tests and `test/resources` for test data

## Setup

```bash
pip install -e .
pip install -r requirements.txt
```

## Tests

```bash
pytest test/ -v
```

## Style

See `../amilib/docs/style_guide_compliance.md`: absolute imports, empty `__init__.py` unless agreed, `Path(Resources.TEMP_DIR, ...)` for temp paths, assert (not return False) in tests, no mocks.
