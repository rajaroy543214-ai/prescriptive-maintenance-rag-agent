import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="data/chroma_db")

# Get collection
collection = client.get_collection("maintenance_manual")


def retrieve(query, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results["documents"][0]


if __name__ == "__main__":
    query = input("Enter your maintenance query: ")

    results = retrieve(query)

    print("\nRelevant information:\n")

    for i, doc in enumerate(results, 1):
        print(f"--- Result {i} ---")
        print(doc)
        print()
