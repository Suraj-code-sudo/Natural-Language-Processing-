import requests

API_KEY_ASSEMBLY = "525723728d2e43d1bea63d255f7ac115"
headers = {'authorization': API_KEY_ASSEMBLY}

audio_url = 'https://cdn.assemblyai.com/upload/6df4f875-c564-4c3e-8139-140012ce7270'

json = {'audio_url':audio_url}
response = requests.post("https://api.assemblyai.com/v2/transcript", json=json, headers=headers)
print(response.json())