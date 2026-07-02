# CSV Inspector

A small command-line tool that reports a CSV file's data-row count, column
names, and first five data rows. It reads values as text without transforming,
filtering, or profiling them.

## Prerequisites

- Python 3.14 or later
- A UTF-8 encoded CSV file with a header row

No third-party packages are required.

## Run

From the project directory, supply exactly one CSV file path:

```powershell
uv run main.py <csv-file>
```

For example:

```powershell
uv run main.py data/test.csv
```

The output labels the data-row count, ordered column names, and preview. A
header-only file has a row count of zero and no rows beneath `Preview:`.
