# 02-file_handling

## Learning goals

- Read and write text files safely.
- Use `os` and `pathlib` for path operations.
- Explain copy, rename, and archive basics.

## Key definitions

- `Path`: a location to a file or directory.
- `File mode`: read/write behavior (`r`, `w`, `a`).
- `Context manager`: pattern using `with` for safe resource cleanup.

## Core concepts

- Use `with open(...)` to auto-close files.
- Prefer `pathlib.Path` for cleaner path code.
- Use `shutil` and `zipfile` for filesystem operations.
- Verify files exist before destructive operations.

## Common mistakes

- Forgetting to close files.
- Using relative paths without knowing current working directory.
- Overwriting files unintentionally with `w` mode.

## Quick recap

- Open/read/write safely.
- Use path utilities instead of hardcoded strings.
- Add existence checks before file operations.
