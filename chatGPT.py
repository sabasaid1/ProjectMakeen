import openai #importing open ai lib
openai.api_key = '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' 
messages = []
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})