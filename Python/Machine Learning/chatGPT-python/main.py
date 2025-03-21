import openai

openai.api_key = "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"

chat_history = []

while True:
    prompt = input("Enter a prompt: ")
    if prompt == "exit":
        break
    else:
        chat_history.append({"role": "user", "content": prompt})

        response_iterator = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            stream=True,
            max_tokens=150,
        )

        collected_messages = []

        for chunk in response_iterator:
            chunk_message = chunk['choices'][0]['delta']  # extract the message
            collected_messages.append(chunk_message)  # save the message
            full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
            print(full_reply_content)

            # clear the terminal
            print("\033[H\033[J", end="")

        chat_history.append({"role": "assistant", "content": full_reply_content})
        # print the time delay and text received
        full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
        print(f"GPT: {full_reply_content}")


