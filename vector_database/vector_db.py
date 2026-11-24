"""Store a small set of example documents in a local Chroma database."""

from pathlib import Path

import chromadb

# Create a local vector database
store_path = Path(__file__).resolve().parent / "vector_store"
client = chromadb.PersistentClient(path=str(store_path))

# Create a collection
collection = client.get_or_create_collection(
    name="rag_documents"
)

# Store documents
collection.upsert(
    ids=["1", "2"],
    documents=[
        "Python is a programming language.",
        "FastAPI is a Python web framework."
    ]
)

print("Documents stored successfully!")
