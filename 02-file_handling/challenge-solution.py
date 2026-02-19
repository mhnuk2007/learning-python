"""Challenge: total byte size of .txt files in deps/."""

from pathlib import Path


def ensure_sample_deps(deps_dir: Path) -> None:
    deps_dir.mkdir(exist_ok=True)

    sample_files = {
        "a.txt": "hello\n",
        "b.txt": "world\n",
    }

    for filename, content in sample_files.items():
        sample_path = deps_dir / filename
        if not sample_path.exists():
            sample_path.write_text(content, encoding="utf-8")


def file_info() -> tuple[int, list[Path]]:
    """Calculate the total size in bytes of all .txt files inside deps/."""
    base_dir = Path(__file__).resolve().parent
    deps_dir = base_dir / "deps"

    ensure_sample_deps(deps_dir)

    text_files = [p for p in deps_dir.glob("*.txt") if p.is_file()]
    total_bytes = sum(p.stat().st_size for p in text_files)

    return total_bytes, text_files


if __name__ == "__main__":
    total, files = file_info()
    print("Text files in deps:")
    for file in files:
        print(f"- {file.name}: {file.stat().st_size} bytes")
    print("Total bytes of .txt files in deps:", total)
