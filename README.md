# Cursor AI Student Report Refactoring

This project contains the Lecture 6 messy Python report program before and after a readability refactor.

- `messy_before.py` preserves the original Colab code.
- `messy.py` is the readable refactor.
- `original_output.txt` records the reference output from the original program.
- `.cursor/rules/python-standards.mdc` contains the course rules used for the final review.

Run the final program with:

```bash
python messy.py
```

The refactor uses descriptive names, reusable functions, a named subject-count constant, f-strings, and no unused imports. Its printed output remains character-for-character identical to the reference output.
