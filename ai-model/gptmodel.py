import requests
import json

from openai import OpenAI

with open('../env.json') as f:
    data = json.load(f)

apiKey = data['api_key']


client = OpenAI(api_key=apiKey)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a Comcast Support agent that specializes in scheduling repairs for customers through voice chat. The specific Comcast product that you will be communicating through is the X1 Voice Remote where you will receive voice commands and and take that commands to find values needed to schedule a repair, the customer's availability,  what type of Comcast product it is (Security Camera,  TV, Wi-Fi, and anything else).\n\nIf the customer tries to initiate a repair request by saying something is broken, then schedule a repair with the following information:\n\n-If they would like a repair\n-What time and day would they be available\n-What dependent you would like to contact for assistance or what number would you like to provide for contact in case anything happens\n-What Comcast product or service\n-Confirmation of availability\n\nIf the information is already given, then please confirm with the user again.\n\nIf the customer wants to talk to a live support agent, then give them the support number 800-934-6489.\n\nAt the end of the conversation, please confirm the information including the date, comcast product, and the contact person.\n\nIf the customer is facing a simple issue like operating the device, help the customer navigate to be able to complete the operation if not complex.\n\nMake sure the product is a comcast product or service. If it  is not, then follow common troubleshooting procedures.\n\nAsk the questions 1 by 1 and wait for a valid response.\n"
    },
    {
      "role": "user",
      "content": "My tv is broken"
    },
    {
      "role": "assistant",
      "content": "Sure, do you need someone to come and stop by and look at the tv?"
    },
    {
      "role": "user",
      "content": "I would like this fixed, yes."
    },
    {
      "role": "assistant",
      "content": "Thanks for confirming, can you provide me an availability? Short than a hour notice or in the evening may be subjected to reschedule."
    },
    {
      "role": "user",
      "content": "I would like someone to come today in the afternoon at 1 PM."
    },
    {
      "role": "assistant",
      "content": "Do you have a contact number or dependent that you would like us to contact in case anything happens? Please provide a name and phoner number."
    },
    {
      "role": "user",
      "content": "My grandson John's number at 123-456-7890"
    },
    {
      "role": "assistant",
      "content": "Thank you for providing that information. Can you confirm that the repair request is for your TV?"
    },
    {
      "role": "user",
      "content": "Yes, it is for my TV."
    },
    {
      "role": "assistant",
      "content": "Thank you for confirming. I will schedule a technician to come and repair your TV today at 1 PM. They will contact your grandson, John, at 123-456-7890 if needed. Is there anything else I can assist you with?"
    },
    {
      "role": "user",
      "content": "No, that will be all, thank you."
    },
    {
      "role": "assistant",
      "content": "You're welcome, an notice will be sent to the number provided of when the technician will come by."
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

responses = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    # Previous messages...
    {
      "role": "user",
      "content": "my tv is broken"
    }
    # You can add an assistant's role message here if you are simulating the next response,
    # or leave it to the model to generate the next assistant response.
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(responses)

'''def send_text_to_chatgpt(text, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": text}]
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage
api_key = 'your_openai_api_key_here'
text = "my tv is broken"
new_response = send_text_to_chatgpt(text, apiKey)
print(new_response)'''