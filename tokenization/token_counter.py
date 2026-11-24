import tiktoken

text = "I am learning RAG engineering with Python."

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Text:", text)
print("Tokens:", tokens)
print("Token count:", len(tokens))