# pip install openai
import openai

# La user_key varia depende el usuario y debe generarse desde https://openai.com/product

openai.api_key = "(user_key)"


while True:
    prompt = input("\ningrese su preguntra: " )

    if prompt == "exit":
        break

    answer = openai.Completion.create(engine="text-davinci-003",
                                                prompt=prompt,
                                                max_tokens=2048)

    print(answer.choices[0].text)
