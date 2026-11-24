
from pathlib import Path

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Define project paths
BASE_DIR = Path(__file__).parent

PDF_PATH = BASE_DIR / "documents" / "fastapi_tutorial.pdf"
DB_PATH = BASE_DIR / "vector_store"


# 2. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 3. Configure the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


# 4. Load PDF and extract text
reader = PdfReader(str(PDF_PATH))

chunks = []
metadatas = []

for page_number, page in enumerate(reader.pages, start=1):

    page_text = page.extract_text() or ""

    page_chunks = splitter.split_text(page_text)

    for chunk_number, chunk in enumerate(page_chunks):

        chunks.append(chunk)

        metadatas.append({
            "source": PDF_PATH.name,
            "page": page_number,
            "chunk": chunk_number
        })


# 5. Generate embeddings
if not chunks:
    raise ValueError("No text extracted from the PDF.")

embeddings = model.encode(
    chunks,
    normalize_embeddings=True
).tolist()


# 6. Connect to ChromaDB
client = chromadb.PersistentClient(
    path=str(DB_PATH)
)

collection = client.get_or_create_collection(
    name="rag_documents",
    metadata={"hnsw:space": "cosine"}
)


# 7. Store chunks and embeddings
ids = [
    f"{PDF_PATH.stem}-page-{meta['page']}-chunk-{meta['chunk']}"
    for meta in metadatas
]

collection.upsert(
    ids=ids,
    documents=chunks,
    embeddings=embeddings,
    metadatas=metadatas
)


print("Ingestion completed successfully!")
print("Total chunks:", len(chunks))
print("Total vectors stored:", collection.count())
