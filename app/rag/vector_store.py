from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from app.parser.parser import load_manual
from app.parser.chunker import chunk_text


DB_PATH = "data/chroma_db"
COLLECTION_NAME = "maintenance_manual"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


def build_vector_store():
    manual_path = "data/manuals/machine_manual.txt"

    text = load_manual(manual_path)
    chunks = chunk_text(text)

    embeddings = model.encode(chunks).tolist()

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"Successfully stored {len(chunks)} chunks in ChromaDB.")


if __name__ == "__main__":
    build_vector_store()
