import json
from openai import OpenAI

with open('env.json') as f:
    data = json.load(f)

apiKey = data['api_key']

client = OpenAI(api_key=data)

client.files.create(
  file=open("comcast_support_custom_training.jsonl", "rb"),
  purpose="fine-tune"
)