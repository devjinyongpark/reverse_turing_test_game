from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_random_questions(number_of_question: int = 20) -> list[str]:
    if number_of_question <= 0:
        raise ValueError("number_of_question must be greater than 0")

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "system",
                "content": (
                    "You generate strictly formatted output. "
                    "You must follow the user's format exactly."
                ),
            },
            {
                "role": "user",
                "content": f"""
Generate exactly {number_of_question} unique questions for a Reverse Turing Test game.

Output requirements:
- Return ONLY a valid JSON array.
- The array must contain exactly {number_of_question} items.
- Each item must be a string.
- Each string must be a unique question.
- Do not include numbering.
- Do not include markdown.
- Do not include code fences.
- Do not include explanations, titles, notes, or extra text.
- Every item must end with a question mark.

Example format:
["Question 1?", "Question 2?", "Question 3?"]
""".strip(),
            },
        ],
        temperature=0.3,
    )

    raw_text = response.output_text.strip()

    try:
        questions = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Model did not return valid JSON:\n{raw_text}") from e

    if not isinstance(questions, list):
        raise ValueError("Model output is not a JSON list")

    if len(questions) != number_of_question:
        raise ValueError(
            f"Expected {number_of_question} questions, got {len(questions)}"
        )

    if not all(isinstance(q, str) for q in questions):
        raise ValueError("All items in the output must be strings")

    questions = [q.strip() for q in questions]

    if len(set(questions)) != len(questions):
        raise ValueError("Questions are not unique")

    if not all(q.endswith("?") for q in questions):
        raise ValueError("Every question must end with a question mark")

    return questions

def save_random_questions(questions: list[str]) -> None:
    filename = "questions.txt"

    with open(filename, 'a') as file:
        for q in questions:
            file.write(q + "\n")

if __name__ == "__main__":
    questions = generate_random_questions()
    save_random_questions(questions)