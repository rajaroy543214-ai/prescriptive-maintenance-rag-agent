from pathlib import Path


def load_manual(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Manual not found: {file_path}")

    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    manual_path = "data/manuals/machine_manual.txt"

    text = load_manual(manual_path)

    print("Manual loaded successfully!")
    print(f"Characters: {len(text)}")
    print("\nFirst 500 characters:\n")
    print(text[:500])
