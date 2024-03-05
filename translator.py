import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
import gtts 
import playsound


def take_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return format(text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text
voice_input_text = take_voice_input()
translated_text = translate_text(voice_input_text, target_language='en')
sound = gtts.gTTS(translated_text,lang='en')
sound.save('intro.mp3')
playsound.playsound('intro.mp3')