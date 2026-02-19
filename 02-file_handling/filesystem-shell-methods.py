"""Copy, rename, and archive file operations demo."""

from pathlib import Path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def ensure_example_file(example_path: Path) -> None:
    if example_path.exists():
        return

    example_path.write_text("First line\nSecond line\n", encoding="utf-8")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    original_file = base_dir / "example.txt"
    backup_file = base_dir / "example.txt.bak"
    renamed_file = base_dir / "example_renamed.txt"
    archive_path = base_dir / "archive.zip"
    custom_zip_path = base_dir / "testzip.zip"

    ensure_example_file(original_file)
    print("Source file:", original_file)

    if backup_file.exists():
        backup_file.unlink()
    shutil.copy2(original_file, backup_file)
    print("Backup created:", backup_file)

    if renamed_file.exists():
        renamed_file.unlink()
    original_file.rename(renamed_file)
    print("File renamed to:", renamed_file)

    if archive_path.exists():
        archive_path.unlink()
    make_archive(str(base_dir / "archive"), "zip", base_dir)
    print("Archive created:", archive_path)

    if custom_zip_path.exists():
        custom_zip_path.unlink()
    with ZipFile(custom_zip_path, "w") as newzip:
        newzip.write(renamed_file, arcname=renamed_file.name)
        newzip.write(backup_file, arcname=backup_file.name)
    print("Custom ZIP created:", custom_zip_path)

    # Restore the original file so reruns are deterministic.
    shutil.copy2(renamed_file, original_file)


if __name__ == "__main__":
    main()
