from groq import Groq
api_key = "use your own "
client = Groq(api_key=api_key)
while True:
    user = input( "Enter Your Question: ")
    if user.lower() == "exit":
        print("Goodbye")
        break
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
                {
                    "role": "user",
                    "content": user
                }
        ]
    )
    print(completion.choices[0].message.content) 