import speech_recognition as sr
import openai
import json

# Replace 'your-api-key' with your actual OpenAI API key
with open("env.json", "r") as file:
    key = json.load(file)

openai.api_key = key['api_key']

# Replace 'your-model-name' with your actual model name
MODEL_NAME = 'ft:gpt-3.5-turbo-1106:personal::9GH0rlW2'

# Initialize the recognizer
r = sr.Recognizer()

conversation_histories = {
    "userresponses": "",
    "modelresponses": ""
}

conversation_history = []

# Function to convert voice to text and send to the GPT model
'''def listen_and_query_gpt():
    with sr.Microphone() as source:
        print("Speak anything:")
        audio_data = r.listen(source)
        print("Recognizing...")
        try:
            # Convert audio to text
            text = r.recognize_google(audio_data).lower()
            print(f"You said: {text}")
            if text in ["stop", "quit", "exit"]:
                return text, True  # Return the text and True to indicate that we need to stop the loop
            else:
                # Send text to OpenAI GPT model using the chat completion endpoint
                conversation_history.append(text)
                response = openai.ChatCompletion.create(
                    model=MODEL_NAME,
                    messages=[{"role": "user", "content": text}]
                )
                # Print the GPT model's response
                print(response.choices[0].message['content'])
                return text, False
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None, False
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None, False
        except openai.error.OpenAIError as e:
            print(f"Error in querying OpenAI API; {e}")
            return None, False
        except KeyboardInterrupt as e:
            print("Exiting the program.")
            return None, False'''

# second solution
'''
def listen_and_query_gpt():
    with sr.Microphone() as source:
        print("Speak anything:")
        audio_data = r.listen(source)
        print("Recognizing...")
        try:
            # Convert audio to text
            text = r.recognize_google(audio_data).lower()
            print(f"You said: {text}")
            if text in ["stop", "quit", "exit"]:
                return text, True  # Return the text and True to indicate that we need to stop the loop
            else:
                # Append the user's message to the conversation history
                conversation_history.append({"role": "user", "content": text})
                
                # Send the entire conversation history to the model
                response = openai.ChatCompletion.create(
                    model=MODEL_NAME,
                    messages=conversation_history
                )
                
                # Get the model's response
                model_response = response.choices[0].message['content']
                print(model_response)
                
                # Append the model's response to the conversation history
                conversation_history.append({"role": "assistant", "content": model_response})
                
                return text, False
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None, False
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None, False
        except openai.error.OpenAIError as e:
            print(f"Error in querying OpenAI API; {e}")
            return None, False
'''

def listen_and_query_gpt():
    with sr.Microphone() as source:
        print("Speak anything:")
        audio_data = r.listen(source)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio_data).lower()
            print(f"You said: {text}")
            if text in ["stop", "quit", "exit"]:
                return text, True

            # Check if the user said "broken", if so, tailor the prompt to scheduling a repair
            if "broken" in text:
                prompt_text = "The customer has indicated a broken device and needs to schedule a repair."
            else:
                prompt_text = text

            # Append the user's message to the conversation history with the tailored prompt
            conversation_history.append({"role": "user", "content": prompt_text})

            # Send the entire conversation history to the model
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=conversation_history
            )
            model_response = response.choices[0].message['content']
            print(model_response)

            # Append the model's response to the conversation history
            conversation_history.append({"role": "assistant", "content": model_response})

            return text, False
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None, False
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None, False
        except openai.error.OpenAIError as e:
            print(f"Error in querying OpenAI API; {e}")
            return None, False
        
# Loop to continue listening, converting, and querying GPT
while True:
    text, should_stop = listen_and_query_gpt()
    if should_stop:
        print("Exiting the program.")
        break

print(conversation_history)