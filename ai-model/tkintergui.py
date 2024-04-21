'''import tkinter as tk
import customtkinter as ctk
import speech_recognition as sr
import openai
import json
import threading

# Function to set up the OpenAI API key
def setup_openai_api():
    with open("env.json", "r") as file:
        key = json.load(file)
    openai.api_key = key['api_key']

# Replace 'your-model-name' with your actual model name
MODEL_NAME = 'ft:gpt-3.5-turbo-0125:personal::9GQjHdV4'

# Initialize the recognizer
r = sr.Recognizer()

# Create the main window
app = ctk.CTk()
app.title('Voice to GPT Chat')
app.geometry('600x500')

# Function to process and display model responses
# Function to process and display responses
def display_response(sender, message):
    chat_history.configure(state=tk.NORMAL)
    message_to_display = f"{sender}: {message}\n"
    chat_history.insert(tk.END, message_to_display)
    chat_history.insert(tk.END, "\n")
    chat_history.see(tk.END)  # Scroll to the end of the chat history
    chat_history.configure(state=tk.DISABLED)

message_list = []
is_listening = False

# Function to toggle listening mode
def toggle_listening():
    global is_listening, listen_button

    # If currently not listening, start listening
    if not is_listening:
        is_listening = True
        listen_button.configure(text="Stop Listening", fg_color="red")
        listen_button.after(100, start_listening)  # Add a slight delay before starting to listen
    else:
        is_listening = False
        listen_button.configure(text="Listen", fg_color=ctk.ThemeManager.theme["color"]["button"])

# Function that handles the actual listening and processing
def start_listening():
    def recognize_speech():
        global is_listening
        try:
            while is_listening:
                with sr.Microphone() as source:
                    audio_data = r.listen(source)
                    text = r.recognize_google(audio_data).lower()
                    app.after(0, display_response, "You", text)
                    message_list.append(text)
                    response = openai.ChatCompletion.create(
                        model=MODEL_NAME,
                        messages=[{"role": "user", "content": text}]
                    )
                    model_response = response.choices[0].message['content']
                    app.after(0, display_response, "Comcast AI Support", model_response)
                    message_list.append(model_response)
        except Exception as e:
            app.after(0, display_response, "Error", str(e))
        finally:
            # Reset the listen button when stopping listening
            app.after(0, lambda: listen_button.configure(text="Listen", fg_color=ctk.ThemeManager.theme["color"]["button"]))
            is_listening = False

    # Start the listening process in a new thread
    if is_listening:
        thread = threading.Thread(target=recognize_speech)
        thread.start()

# Chat history text area
chat_history = ctk.CTkTextbox(app, height=200, width=300, state=tk.DISABLED)
chat_history.pack(pady=50)

# Listen button
listen_button = ctk.CTkButton(app, text="Listen", command=toggle_listening)
listen_button.pack()

# Run the setup for OpenAI API key
setup_openai_api()

# Start the main GUI loop
app.mainloop()

print(message_list)'''

import tkinter as tk
import customtkinter as ctk
import speech_recognition as sr
import openai
import json
import threading
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(text)
    engine.runAndWait()

# Function to set up the OpenAI API key
def setup_openai_api():
    with open("env.json", "r") as file:
        key = json.load(file)
    openai.api_key = key['api_key']

# Replace 'your-model-name' with your actual model name
MODEL_NAME = 'ft:gpt-3.5-turbo-0125:personal::9GQjHdV4'

# Initialize the recognizer
r = sr.Recognizer()

message_list = {
    "User": "",
    "AI": ""
}

empty_string = []
AI_string = []

# Create the main window
app = ctk.CTk()
app.title('Voice to GPT Chat')
app.geometry('600x500')

# Global variable to track whether the app is currently listening
is_listening = False

# Function to process and display responses
def display_response(sender, message):
    chat_history.configure(state=tk.NORMAL)
    message_to_display = f"{sender}: {message}\n"
    chat_history.insert(tk.END, message_to_display)
    chat_history.insert(tk.END, "\n")
    chat_history.see(tk.END)  # Scroll to the end of the chat history
    chat_history.configure(state=tk.DISABLED)

def toggle_listening():
    global is_listening, listen_button

    if not is_listening:
        is_listening = True
        listen_button.configure(text="Stop Listening", fg_color="red")
        listen_button.after(100, start_listening)
    else:
        is_listening = False
        # Set the color directly to a shade of blue you prefer
        listen_button.configure(text="Listen", fg_color="#3498db")  # Example blue color

# Adjusted function for handling actual listening and processing
def start_listening():
    def recognize_speech():
        global is_listening
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise at the beginning of the session
                r.adjust_for_ambient_noise(source, duration=1)
                while is_listening:
                    try:
                        # Listening for the user's speech with adjusted timeout values
                        audio_data = r.listen(source, timeout=10, phrase_time_limit=10)
                        text = r.recognize_google(audio_data).lower()
                        empty_string.append(text)
                        app.after(0, display_response, "You", text)
                    except sr.WaitTimeoutError:
                        # Handling the case where no speech was detected within the timeout period
                        app.after(0, display_response, "Error", "I didn't catch that. Could you please say it again?")
                        continue

                    # Making a call to the OpenAI API with the recognized text
                    try:
                        response = openai.ChatCompletion.create(
                            model=MODEL_NAME,
                            messages=[{"role": "user", "content": text}]
                        )
                        model_response = response.choices[0].message['content']
                        AI_string.append(model_response)
                        speak(model_response)
                        app.after(0, display_response, "Comcast AI Support", model_response)
                    except Exception as api_error:
                        # Handling potential errors from the API call
                        app.after(0, display_response, "Error", str(api_error))
                    
        except Exception as e:
            start_listening()
        finally:
            # Ensuring the UI is reset when listening stops
            if not is_listening:
                app.after(0, lambda: listen_button.configure(text="Listen", fg_color="#3498db"))  # Reverting to the default color

    if is_listening:
        thread = threading.Thread(target=recognize_speech)
        thread.start()


# Chat history text area
chat_history = ctk.CTkTextbox(app, height=200, width=600, state=tk.DISABLED)
chat_history.pack(pady=50)

# Listen button
listen_button = ctk.CTkButton(app, text="Listen", command=toggle_listening)
listen_button.pack()

# Run the setup for OpenAI API key
setup_openai_api()

# Start the main GUI loop
app.mainloop()

message_list["User"] = empty_string

message_list["AI"] = AI_string


json_object = json.dumps(message_list, indent=4)

with open("messagelist.json", "w") as outfile:
    outfile.write(json_object)
