import os
import re
from dotenv import load_dotenv
from groq import Groq

from llm.memory import ConversationMemory
from llm.user_memory import remember, recall

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

memory = ConversationMemory()


def extract_user_information(prompt):
    text = prompt.lower()

    # Remember user's name
    if "my name is" in text:
        match = re.search(r"my name is\s+(.+)", prompt, re.IGNORECASE)
        if match:
            name = match.group(1).strip(" .")
            remember("name", name)

    # Remember user's city
    if "i am from" in text:
        match = re.search(r"i am from\s+(.+)", prompt, re.IGNORECASE)
        if match:
            city = match.group(1).strip(" .")
            remember("city", city)


def get_gemini_response(prompt):

    try:

        text = prompt.lower()

        # Store user information
        extract_user_information(prompt)

        # Answer directly from persistent memory
        if "what is my name" in text or "what's my name" in text:

            name = recall("name")

            if name:
                return f"Your name is {name}."

        if "where am i from" in text:

            city = recall("city")

            if city:
                return f"You are from {city}."

        # Add user message to conversation
        memory.add_user(prompt)

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=memory.get_messages(),

            temperature=0.6,

            max_tokens=300

        )

        answer = response.choices[0].message.content

        memory.add_assistant(answer)

        return answer

    except Exception:

        return "Sorry, I couldn't connect to Groq."


from llm.user_memory import clear_user_memory


def clear_memory():

    memory.clear()

    clear_user_memory()