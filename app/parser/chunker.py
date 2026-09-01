def chunk_text(text: str, chunk_size: int = 500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size].strip()

        if chunk:
            chunks.append(chunk)

    return chunks


if __name__ == "__main__":
    from parser import load_manual

    text = load_manual("data/manuals/machine_manual.txt")
    chunks = chunk_text(text)

    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks, 1):
        print(f"\n--- Chunk {i} ---")
        print(chunk)
