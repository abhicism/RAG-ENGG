
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

def main() -> None:
    load_dotenv(Path(__file__).resolve().parent / ".env")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Set it in the environment or in llm_integration/.env."
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-5.4",
        input="Explain Python in simple language.",
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
