# Sprint 1: Basic CSV Inspection

## Problem Statement

Users need a quick way to understand the basic structure and contents of a CSV
file without opening it in a spreadsheet or writing code. Build a small Python
command-line tool that accepts a CSV file path and prints a concise summary of
the file.

## Sprint Goal

Deliver a runnable, documented CSV inspection tool that reports the file's row
count, column names, and first five data rows, with clear messages for common
input errors.

## User Requirements

1. The user can provide the path to a CSV file when running the tool.
2. The tool reports the number of data rows in the CSV file. The header row is
   not included in this count.
3. The tool reports the column names in their original order.
4. The tool displays the first five data rows in their original column order.
   If the file has fewer than five data rows, it displays all available rows.
5. The README contains the prerequisites, the command needed to run the tool,
   and an example using a CSV file path.
6. Common failures produce concise, user-friendly error messages rather than a
   Python traceback.

## Expected Command-Line Behavior

- The CSV path is supplied as a command-line argument.
- Successful output clearly labels the row count, column names, and preview.
- CSV values are displayed as read; this sprint does not infer or convert data
  types.
- A header-only CSV reports zero data rows and an empty preview.

## Plan

1. Add command-line handling for a single CSV file path.
2. Read the file with Python CSV support and preserve the source column order.
3. Count all data rows while retaining no more than the first five for the
   preview.
4. Print a labeled summary containing the row count, column names, and preview.
5. Handle basic input and parsing failures with clear error messages and a
   non-zero exit status.
6. Add concise setup and run instructions to the README.

## Tasks

- [ ] Accept a CSV path from the command line.
- [ ] Validate that a path was provided and that it identifies a readable file.
- [ ] Read the CSV header and report column names in source order.
- [ ] Count data rows without counting the header.
- [ ] Capture and display up to the first five data rows.
- [ ] Format successful output with clear labels.
- [ ] Return user-friendly errors for missing arguments, missing or unreadable
      files, empty files or files without a usable header, and CSV parsing
      failures.
- [ ] Document prerequisites and the run command in the README, including one
      example CSV path.
- [ ] Verify behavior with a normal CSV, a CSV with fewer than five data rows, a
      header-only CSV, and representative error cases.

## Out of Scope

- Editing or transforming CSV data.
- Filtering, sorting, searching, or selecting columns.
- Statistical summaries, data profiling, or data-type inference.
- Support for non-CSV formats such as Excel, JSON, or databases.
- Interactive prompts, graphical interfaces, or web interfaces.
- Configurable preview length; the preview is fixed at five data rows.
- Advanced CSV dialect detection or encoding recovery.
- Performance optimization for unusually large files beyond reading rows
  sequentially.

## Definition of Done

Sprint 1 is complete when all of the following are true:

- Running the documented command with a valid CSV path prints the data-row
  count, ordered column names, and up to the first five data rows.
- The row count excludes the header and remains correct when more than five data
  rows are present.
- Files with fewer than five data rows, including header-only files, are handled
  without failure and produce the expected smaller preview.
- Missing arguments, inaccessible files, unusable empty/header input, and basic
  CSV parsing errors produce understandable messages without a traceback and
  return a non-zero exit status.
- The README provides sufficient prerequisites and commands for a new user to
  run the tool against a CSV file.
- The implementation stays within the boundaries listed in this specification.
