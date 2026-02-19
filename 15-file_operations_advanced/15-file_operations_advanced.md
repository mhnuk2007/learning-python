# 15-file_operations_advanced

## Learning goals

- Work with structured file formats such as JSON and CSV.
- Use `pathlib` and context managers for robust workflows.

## Key definitions

- `Serialization`: converting objects to a storable format.
- `JSON`: text format for structured data.
- `CSV`: tabular text format with delimiters.

## Core concepts

- Use `json.dump/load` for JSON writing/reading.
- Use `csv.DictWriter` and `csv.DictReader` for table-like data.
- Keep output paths explicit and organized.

## Common mistakes

- Mixing numeric and string types inconsistently in CSV/JSON flows.
- Hardcoding absolute paths that break on other machines.

## Quick recap

- Structured file handling is key for data exchange and automation.
