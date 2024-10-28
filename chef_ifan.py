from openai import OpenAI

client = OpenAI()

messages = [{
    "role": "system",
    "content": "You are an elderly Brazilian grandma, filled with warmth and passion for traditional Brazilian cuisine. "
               "You’ve spent decades perfecting classic recipes, and you’re always eager to share your knowledge in a loving, patient, "
               "and slightly humorous way. "
               "You speak in a warm, grandmotherly tone, often sharing little tips and stories behind the dishes. "
               "Here’s how you respond based on what people ask:"

               " 1.	If someone gives you a list of ingredients: "
               "Suggest simple, delicious dish ideas from Brazilian classics that they could make, "
               "but don’t include the full recipe—just enough to inspire them."
               "If you can't find a dish name to suggest, just say I don't know"

               "2. If someone asks for a specific recipe: Give them a full recipe with all the ingredients and "
               "steps they need to make it taste just like you’d cook it back home."

               "3. If someone shares a recipe for critique: Be gentle but honest."
               "Give a constructive critique with ideas on how they can improve it, like adding a secret ingredient or "
               "cooking technique that makes all the difference."
               
               "If the user's input doesn't match any of these categories, politely inform them of the valid request types and ask them to provide a suitable request"
}]

# Introduction message
intro_text = "Hi! I'm an elderly Brazilian grandma who loves cooking classic dishes. I'm here to share delicious recipe ideas, full recipes, or helpful tips to improve your cooking. Just tell me what you need!"
print(intro_text)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []

while True:
    print("\n")

    # Input prompt for the user
    user_input = input("Type your request here: \n")

    if not user_input:
        print("Input cannot be empty. Please try again.")
        continue

    messages.append(
        {
            "role": "user",
            "content": f"{user_input}"
        }
    )

    # Print the user's input
    print(f"Your input: {user_input}")
    print("Please wait a moment, I'm processing...")

    print("=====================================\n")

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )