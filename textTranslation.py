from openai import OpenAI
client = OpenAI()

with open("./output/output1.txt", "r") as text:
    text_en = text.read()

text_jp = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "user", "content": "次に示す文章を全て日本語に翻訳してください" + text_en},
    ],
)

# print(text_jp.choices[0].message.content)

with open("./output/outputs_jp.txt", "w") as file:
    file.write(text_jp.choices[0].message.content)