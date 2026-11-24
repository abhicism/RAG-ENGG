text = "Python is useful for backend and AI development"  # Define the source text

words = text.split()  # Split the text into individual words

chunk_size = 5  # Set the maximum number of words in each chunk
overlap = 2  # Set the number of overlapping words between chunks

chunks = []  # Store the generated text chunks

step = chunk_size - overlap  # Calculate the distance between chunk starting positions

for i in range(0, len(words), step):  # Iterate through the words in chunk-sized steps
    chunk = words[i:i + chunk_size]  # Select a chunk of words
    chunks.append(" ".join(chunk))  # Combine the chunk words into a string

for chunk in chunks:  # Iterate through each generated chunk
    print(chunk)  # Print the chunk