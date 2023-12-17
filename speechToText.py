from openai import OpenAI
client = OpenAI()

audio_file= open("./src/splitAudioPart2.mp3", "rb")

transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
)

# translation = client.chat.completions.create(
#     model="gpt-4-1106-preview",
#     messages=[
#         {"role": "user", "content": "こんにちは。API呼び出しのテストです。何か発言お願いします。"}
#     ],
#     response_format="text"
# )

with open("./output/output2.txt", "w") as file:
    for sentence in transcript.split('.'):
        file.write(sentence.strip() + ".\n")
