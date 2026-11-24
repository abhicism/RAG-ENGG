# Import the SentenceTransformer library
from sentence_transformers import SentenceTransformer

# Load a pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentence we want to convert into numbers
text = "I love Python programming"

# Convert the sentence into a numerical vector
embedding = model.encode(text)

# Print the numerical vector
print(embedding)

# Print the number of dimensions
print(len(embedding))