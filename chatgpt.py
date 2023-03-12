# pip install openai
import openai


openai.api_key = "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"


while True:
    prompt = input("\ningrese su preguntra: " )

    if prompt == "exit":
        break

    answer = openai.Completion.create(engine="text-davinci-003",
                                                prompt=prompt,
                                                max_tokens=2048)

    print(answer.choices[0].text)
