# RAG Engineering

Small, runnable examples covering the building blocks of retrieval augmented generation (RAG).

## Project layout

| Folder | Contents |
| --- | --- |
| `text_processing/` | Basic word based text chunking |
| `chunking/` | Recursive character splitting with LangChain |
| `embeddings/` | Sentence embeddings, similarity example, and notes |
| `prompting/` | Prompt construction example |
| `tokenization/` | Token counting example |
| `vector_database/` | ChromaDB persistence example |
| `chapter_08_document_loading/` | Extract text from the sample PDF |
| `llm_integration/` | OpenAI Responses API example |
| `chapter_10_ingestion/` | PDF to chunks to persistent ChromaDB ingestion |

## Setup

Use Python 3.10 or newer. From the project root, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The embedding examples download the `all-MiniLM-L6-v2` model the first time they run. The LLM example also needs `OPENAI_API_KEY` set in the environment or in `llm_integration/.env`.

## Run examples

Paths to input documents and generated vector stores are resolved relative to each script, so the current working directory does not affect them.

```powershell
python chapter_08_document_loading/load_pdf.py
python chapter_10_ingestion/ingestion.py
python embeddings/embedding.py
python embeddings/similarity_demo.py
python vector_database/vector_db.py
```
