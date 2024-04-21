from openai import OpenAI
import json

with open('env.json') as f:
    data = json.load(f)

apiKey = data['api_key']
client = OpenAI(api_key=apiKey)

client.fine_tuning.jobs.create(
  training_file="file-kYwTO8LhKuCFLMTO4xIv4gAO", 
  model="gpt-3.5-turbo"
)