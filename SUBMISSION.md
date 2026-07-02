# Practicum 3 Submission

Operating system: Windows
Terminal used: Git Bash
Codex tool used: Codex CLI through PowerShell
GitHub repository URL:

## Setup notes

Project folder path: /c/Users/Mze0069/insy7970-sprint-practicum

Starting command: uv run main.py

Starting result: uv run main.py worked and printed "Hello from insy7970-sprint-practicum!"

Files created by uv init: uv init created a Python project scaffold including main.py, pyproject.toml, README.md, .python-version, uv.lock after running, and a Git repository. It also created a .venv folder for the project environment.

.gitignore confirmation: .gitignore excludes .venv/, **pycache**/, .pytest\_cache/, .ruff\_cache/, .mypy\_cache/, .DS\_Store, environment files, coverage output, build/dist artifacts, editor folders, and \*.pyc files.

## Sprint 1 summary

Codex prompt before editing sprint1.md: Read docs/specs/sprint1.md. Help me expand this into a complete sprint spec with a plan, tasks, out-of-scope items, and a definition of done. Do not edit code yet. Before editing the spec file, summarize what you think Sprint 1 should accomplish.

How I defined the user requirements: I kept Sprint 1 focused on basic CSV inspection. I included the required needs that the user can provide a CSV file path, the tool reports row count, and the project includes run instructions. I added that the tool should report column names and show a small preview of the first few rows.

One thing Codex added to the spec that helped: Codex made the definition of done more specific by adding observable checks, such as confirming the row count excludes the header, preview is limited to five rows, errors are user-friendly, and README instructions work.

Sprint 1 run command: uv run main.py data/test.csv

Sprint 1 result: The command worked. It reported 262 data rows, printed the column names, and showed the first five data rows as a preview.

File inspected: I inspected data/test.csv with head -n 6 data/test.csv. I checked that the header and first five rows matched the program preview.

Definition of done check: Sprint 1 met the definition of done. The tool accepts a CSV path, reports the row count without counting the header, prints the column names, and shows five preview rows. I confirmed the output by comparing it with data/test.csv using head. The README includes run instructions, and the program gives user-friendly errors instead of a Python traceback.

Sprint 1 commit: Implement sprint 1

GitHub push confirmation:

## Sprint 2 summary

Sprint 2 theme:

Codex prompt before editing sprint2.md:

Implementation check process and findings:

Sprint 2 commit:

Sprint 2 push confirmation:

Sprint 2 definition of done check:

## Workflow reflection

## Practicum feedback

## Unresolved question

