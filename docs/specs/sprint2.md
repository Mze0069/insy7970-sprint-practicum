# Sprint 2: Missing-Value Summary

## Problem Statement

Users can inspect the basic structure and contents of a CSV file, but they also
need a quick way to identify columns with incomplete data. Extend the existing
Python command-line CSV inspector to report the number and percentage of
missing cells in each column while preserving all Sprint 1 behavior.

## Sprint Goal

Deliver a backward-compatible enhancement to the CSV inspector that reports a
clear missing-value summary for every column, in addition to the existing row
count, column names, preview, documentation, and error handling.

## User Requirements

1. The user can provide the path to a CSV file when running the tool.
2. The tool reports the number of data rows in the CSV file. The header row is
   not included in this count.
3. The tool reports the column names in their original order.
4. The tool displays the first five data rows in their original column order.
   If the file has fewer than five data rows, it displays all available rows.
5. The tool reports a missing-value summary for every column in header order.
6. For each column, the summary reports both the number of missing cells and
   the percentage of data rows whose cell is missing.
7. An empty string or a value containing only whitespace is treated as
   missing. Other values are not treated as missing or converted.
8. The README documents the prerequisites, command needed to run the tool, an
   example using a CSV file path, and the missing-value summary.
9. Common failures produce concise, user-friendly error messages rather than a
   Python traceback.

## Expected Command-Line Behavior

- The CSV path is supplied as a command-line argument.
- Successful output clearly labels the row count, column names, preview, and
  missing-value summary.
- The missing-value summary lists every column in the same order as the CSV
  header.
- A column's missing count is the number of its data cells that are empty or
  contain only whitespace.
- A column's missing percentage is calculated as:

  `missing count / total data-row count * 100`

- Percentage output uses a consistent, documented format across all columns.
- A header-only CSV reports zero data rows, an empty preview, and zero missing
  cells with 0% missing for every column.
- CSV values are displayed as read in the preview. Whitespace may be inspected
  to determine whether a cell is missing, but values are not trimmed or
  otherwise transformed for display.
- All Sprint 1 command-line behavior and error handling remain available.

## Plan

1. Preserve the existing command-line interface, CSV reading, row counting,
   ordered column reporting, five-row preview, and error handling.
2. Initialize a missing-value counter for each header column.
3. While reading each data row, count cells that are empty or contain only
   whitespace.
4. Calculate each column's missing percentage using the total data-row count,
   with explicit handling for a zero-row file.
5. Print a labeled missing-value summary in header order with a consistent
   percentage format.
6. Update the README to describe and demonstrate the added output.
7. Verify the new summary and regression-test all Sprint 1 behavior.

## Tasks

- [ ] Retain the existing single-path command-line interface.
- [ ] Retain the ordered column names, data-row count, and preview of up to five
      data rows.
- [ ] Retain existing validation, user-friendly errors, and non-zero error exit
      statuses.
- [ ] Track a missing-cell count for every header column while reading the CSV.
- [ ] Count both empty strings and whitespace-only cells as missing.
- [ ] Calculate each missing percentage from the total number of data rows.
- [ ] Avoid division by zero for header-only files and report 0% missing for
      each column.
- [ ] Display each column's missing count and percentage in header order under
      a clear summary label.
- [ ] Use one consistent percentage format for every column.
- [ ] Preserve original values in the preview without trimming or converting
      them.
- [ ] Update the README with the missing-value behavior and example output.
- [ ] Verify a file with no missing values, empty cells, whitespace-only cells,
      multiple missing values in one row, and columns with all values missing.
- [ ] Verify a header-only file and all representative Sprint 1 success and
      error cases.

## Out of Scope

- Editing, filling, deleting, or otherwise transforming CSV data.
- Treating sentinel text such as `NA`, `N/A`, `null`, or `not_available` as
  missing; only empty and whitespace-only cells are missing in this sprint.
- Statistical summaries other than missing-value counts and percentages.
- Data-type inference or conversion.
- Filtering, sorting, searching, or selecting columns.
- Support for non-CSV formats such as Excel, JSON, or databases.
- Interactive prompts, graphical interfaces, or web interfaces.
- Configurable preview length; the preview remains fixed at five data rows.
- Advanced CSV dialect detection or encoding recovery.
- Performance optimization for unusually large files beyond reading rows
  sequentially.

## Definition of Done

Sprint 2 is complete when all of the following are true:

- Every Sprint 1 requirement and expected behavior still works.
- Running the documented command with a valid CSV prints the data-row count,
  ordered column names, up to the first five data rows, and a missing-value
  summary for every column.
- Each missing count includes exactly the empty and whitespace-only cells in
  that column.
- Each missing percentage is based on the total data-row count and is displayed
  consistently.
- A header-only CSV completes successfully and reports zero data rows, an empty
  preview, and zero missing cells with 0% missing for every column.
- Preview values remain unchanged from the source CSV.
- Missing arguments, inaccessible files, unusable empty/header input, and basic
  CSV parsing errors continue to produce understandable messages without a
  traceback and return a non-zero exit status.
- The README gives a new user enough information to run the tool and understand
  the missing-value summary.
- The implementation stays within the boundaries listed in this specification.
