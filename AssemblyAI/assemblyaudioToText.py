API_KEY_ASSEMBLY = "525723728d2e43d1bea63d255f7ac115"

import requests

audio = "E:/NLP/AudioToText/Audio/audio.wav"

def read_file(audio, chunk = 5242880):
    with open(audio, 'rb') as _file:
        while True:
            data = _file.read(chunk)
            if not data:break
            yield data

headers = {'authorization': API_KEY_ASSEMBLY}

response = requests.post("https://api.assemblyai.com/v2/upload", headers=headers, data=read_file(audio))
print(response.json())

