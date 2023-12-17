from openai import OpenAI
client = OpenAI()

audio_file= open("./src/splitAudioPart2.mp3", "rb")

transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
)

with open("./output/output2.txt", "w") as file:
    for sentence in transcript.split('.'):
        file.write(sentence.strip() + ".\n")
