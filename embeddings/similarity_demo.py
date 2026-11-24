from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is a programming language",
    "Python is used for software development",
    "I enjoy playing cricket"
]

# Convert sentences into vectors
embeddings = model.encode(sentences)

# Compare the first sentence with the others
similarities = cosine_similarity(
    [embeddings[0]],
    embeddings[1:]
)

print(similarities)