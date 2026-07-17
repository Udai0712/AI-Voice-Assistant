class ConversationMemory:

    def __init__(self):

        self.messages = [
            {
                "role": "system",
                "content": """
You are a friendly Voice AI Assistant.

Rules:
- Speak naturally.
- Keep answers short.
- Be conversational.
- Explain technical topics simply.
- Remember previous messages.
"""
            }
        ]

    def add_user(self, text):

        self.messages.append(
            {
                "role": "user",
                "content": text
            }
        )

    def add_assistant(self, text):

        self.messages.append(
            {
                "role": "assistant",
                "content": text
            }
        )

    def get_messages(self):

        return self.messages

    def clear(self):

        self.messages = [self.messages[0]]