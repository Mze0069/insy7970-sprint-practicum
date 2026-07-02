# CSV Inspector

A small command-line tool that reports a CSV file's data-row count, column
names, first five data rows, and missing values by column. It reads values as
text without transforming or filtering them.

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

The output labels the data-row count, ordered column names, preview, and
missing-value summary. For example:

```text
Row count: 3
Column names: ['name', 'score']
Preview:
['Ada', '10']
['Grace', ' ']
['Linus', '8']
Missing-value summary:
name: 0 missing (0.00%)
score: 1 missing (33.33%)
```

The summary includes every column in header order. Empty and whitespace-only
cells are missing; text such as `NA`, `N/A`, `null`, and `not_available` is not.
Percentages use two decimal places and are calculated from the total data-row
count. A header-only file has a row count of zero, no rows beneath `Preview:`,
and reports `0 missing (0.00%)` for every column.
