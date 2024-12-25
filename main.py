import os
import webbrowser
import datetime

import speech_recognition as sr

import win32com.client

from chat_assistant import get_intent, chat


def speak(text):
    try:
        print(text)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)

    except Exception as e:
        print(f"Speak method failed. Exception: {e}")

def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print("Listening.....")
            audio = r.listen(source)
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(query)
            return  query
    except Exception as e:
        print(f"take_command method failed. Exception: {e}")

if __name__ == '__main__':
    # print("Hello, I am your Assistant.....")
    speak("Hello, I am your Assistant.....")
    while True:
        command = take_command()
        intent_obj = get_intent(command)
        print(f"get_intent response: {intent_obj}")
        if intent_obj.intent == "open_website":
            if intent_obj.website_url:
                speak(f"Opening {intent_obj.website_name} sir...")
                webbrowser.open(intent_obj.website_url)
                break
            else:
                speak(f"Sorry sir.., could you please provide website name?")
        elif intent_obj.intent == "play_music":
            if intent_obj.music_name:
                speak(f"Playing {intent_obj.website_name} sir...")
                webbrowser.open(f"https://www.youtube.com/results?search_query={intent_obj.music_name}+song")
                break
            else:
                speak(f"Sorry sir.., could you please provide music name?")
        elif intent_obj.intent == "time":
            time = datetime.datetime.now()
            speak(f"Sir time is {time}")

        elif intent_obj.intent == "open_camera":
            os.system('start microsoft.windows.camera:')
            break
        elif intent_obj.intent == "quit":
            break

        else:
            response = chat(command)
            speak(response)

