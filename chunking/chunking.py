
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample document
text = """
FastAPI is a Python framework.
It supports API development.

Pydantic handles data validation.
"""

# Create Recursive Character Text Splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

# Split the text into chunks
chunks = splitter.split_text(text)

# Print the chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}:")
    print(chunk)
    print("----------------")
