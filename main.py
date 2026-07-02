"""Print a structural and missing-value summary of a CSV file."""

import csv
import sys
from pathlib import Path


PREVIEW_SIZE = 5


def inspect_csv(path: Path) -> tuple[list[str], int, list[list[str]], list[int]]:
    """Return the header, row count, preview, and missing counts."""
    with path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.reader(csv_file, strict=True)

        try:
            header = next(reader)
        except StopIteration as error:
            raise ValueError("the CSV file is empty or has no usable header") from error

        if not header or not any(column.strip() for column in header):
            raise ValueError("the CSV file is empty or has no usable header")

        preview: list[list[str]] = []
        missing_counts = [0] * len(header)
        row_count = 0
        for row in reader:
            row_count += 1
            for index in range(len(header)):
                if index >= len(row) or not row[index].strip():
                    missing_counts[index] += 1
            if len(preview) < PREVIEW_SIZE:
                preview.append(row)

    return header, row_count, preview, missing_counts


def main(arguments: list[str] | None = None) -> int:
    """Run the command-line CSV inspector."""
    arguments = sys.argv[1:] if arguments is None else arguments

    if len(arguments) != 1:
        print("Error: provide exactly one CSV file path.", file=sys.stderr)
        print("Usage: uv run main.py <csv-file>", file=sys.stderr)
        return 2

    path = Path(arguments[0])
    if not path.is_file():
        print(f"Error: file not found or is not a readable file: {path}", file=sys.stderr)
        return 1

    try:
        header, row_count, preview, missing_counts = inspect_csv(path)
    except ValueError as error:
        print(f"Error: {error}.", file=sys.stderr)
        return 1
    except csv.Error as error:
        print(f"Error: could not parse CSV file: {error}.", file=sys.stderr)
        return 1
    except UnicodeError:
        print("Error: CSV file is not valid UTF-8 text.", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error: could not read file: {error}.", file=sys.stderr)
        return 1

    print(f"Row count: {row_count}")
    print(f"Column names: {header}")
    print("Preview:")
    for row in preview:
        print(row)
    print("Missing-value summary:")
    for column, missing_count in zip(header, missing_counts):
        missing_percentage = (
            missing_count / row_count * 100 if row_count else 0.0
        )
        print(f"{column}: {missing_count} missing ({missing_percentage:.2f}%)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
