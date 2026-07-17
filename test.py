from llm.gemini import get_gemini_response

question = input("You: ")

response = get_gemini_response(question)

print("\nAI:")
print(response)