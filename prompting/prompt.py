
# Function to create a prompt using a topic and student level
def create_prompt(topic, level):

    # Store the prompt template with placeholders
    template = """
    You are an AI programming tutor.

    Topic: {topic}
    Student Level: {level}

    Explain the topic with:
    1. Definition
    2. Simple explanation
    3. Practical example
    """

    # Replace {topic} and {level} with actual values
    # Return the completed prompt
    return template.format(
        topic=topic,
        level=level
    )


# Call the function with the required topic and level
prompt = create_prompt(
    "Vector Database",
    "Beginner"
)

# Display the generated prompt in the terminal
print(prompt)
