from openai import OpenAI

client = OpenAI(
    api_key='sk-proj-NxQYACsIlM8gR8sha6abT3BlbkFJuHDZjuAlmedrHjJRg6Wa'
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "break"]:
            break

        response = chat_gpt(user_input)
        print("Chatbot: ", response)
