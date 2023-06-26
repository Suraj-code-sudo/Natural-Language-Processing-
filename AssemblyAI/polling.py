import requests

API_KEY_ASSEMBLY = "525723728d2e43d1bea63d255f7ac115"
# {'id': '6x0g6ai5o7-8c30-45e7-87c4-322d0fc8ad43', 'language_model': 'assemblyai_default', 'acoustic_model': 'assemblyai_default', 'language_code': 'en_us', 'status': 'queued', 'audio_url': 'https://cdn.assemblyai.com/upload/6df4f875-c564-4c3e-8139-140012ce7270', 'text': None, 'words': None, 
# 'utterances': None, 'confidence': None, 'audio_duration': None, 'punctuate': True, 'format_text': True, 'dual_channel': None, 'webhook_url': None, 'webhook_status_code': None, 'webhook_auth': False, 'webhook_auth_header_name': None, 'speed_boost': False, 'auto_highlights_result': None, 'auto_highlights': False, 
# 'audio_start_from': None, 'audio_end_at': None, 'word_boost': [], 'boost_param': None, 'filter_profanity': False, 'redact_pii': False, 'redact_pii_audio': False, 'redact_pii_audio_quality': None, 'redact_pii_policies': None, 'redact_pii_sub': None, 'speaker_labels': False, 'content_safety': False, 'iab_categories': False, 'content_safety_labels': {}, 'iab_categories_result': {},
#  'language_detection': False, 'custom_spelling': None, 'throttled': None, 'auto_chapters': False, 'summarization': False, 'summary_type': None, 'summary_model': None, 'custom_topics': False, 'topics': [], 'speech_threshold': None, 'disfluencies': False, 'sentiment_analysis': False, 'sentiment_analysis_results': None, 'chapters': None, 'entity_detection': False, 'entities': None, 'speakers_expected': None}

polling_endpoint = "https://api.assemblyai.com/v2/transcript/6x0g6ai5o7-8c30-45e7-87c4-322d0fc8ad43"
headers = {'authorization': API_KEY_ASSEMBLY}
response = requests.get(polling_endpoint, headers)

print(response.json()['text'])

# How many people are there in your family? There are five people in my family. My father, mother, brother, sister and me. Does your family live in a house or an apartment? We live in a house in the countryside. What does your father do? My father is a doctor. He works at the local hospital. How old is your mother? She is 40 years old. One year younger than my father. Do you have any siblings? What's his or her name? 
# Yes, I do. I have one elder brother, David, and one younger sister, Mary. Are you the oldest among your brothers and sisters? No, I'm not. I'm the second child in my family. What is your mother father like? My father likes playing football and my mother likes cooking. Do your parents let you stay out late? Of course not. They always ask me to get home before 10:00 p.m. Each night. Do you stay with your parents right now? No, but I used to. Does your family usually have dinner together? 
# Yes, we do. My mom always prepares delicious meals for us.
