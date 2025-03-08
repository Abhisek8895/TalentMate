from huggingface_hub import InferenceClient
import os
import re
from dotenv import load_dotenv
from database import fetch_tech_stack

load_dotenv()

api_key = os.getenv("huggingface_api_key")

client = InferenceClient(
    provider= "hf-inference",
    api_key=api_key
)

def question_cleaning(raw_questions):
    questions = re.split(r"\d+\.\s", raw_questions.strip())

    # Remove empty elements (if any)
    questions = [q.strip() for q in questions if q.strip()]

    ques_list = []

    # Get the list
    for question in questions:
        temp_list = question.split(':')
        ques_list.append(temp_list[1])

    return ques_list

def generate_questions(tech_stack):
    # tech_stack = fetch_tech_stack(candidate_id)
    prompt = f"""Generate 5 theoretical interview questions on {tech_stack}.  
            The questions should test conceptual understanding without requiring coding.  
            Do not include coding exercises, debugging scenarios, or practical implementation details.  
            Only ask about fundamental concepts, principles, and theories."""

    messages = [
        {"role": "user", "content": prompt}
    ]

    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3", 
        messages=messages, 
        max_tokens=500,  # Adjust as needed
        temperature=0.8,
        top_p= 0.9
    )

    return completion.choices[0].message.content