import json
import os

FILE_NAME = "user_memory.json"


def load_memory():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {}


def save_memory(memory):

    with open(FILE_NAME, "w") as file:
        json.dump(memory, file, indent=4)


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):

    memory = load_memory()

    return memory.get(key)


def clear_user_memory():

    save_memory({})