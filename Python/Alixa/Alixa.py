import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import speech_recognition as sr


speech = sr.Recognizer()


def alixa(audio):
    text = gTTS(text=audio , lang='en', slow=False)
    file_name='speech.mp3'
    text.save(file_name)
    playsound.playsound(file_name)
    print(audio)
    os.remove(file_name)

def record(rec=False):
    with sr.Microphone(device_index=None) as source:
        speech.adjust_for_ambient_noise(source)
        if rec:
            alixa(rec)
        voice = speech.listen(source)
        voice_data = ""
        try:
            voice_data=speech.recognize_google(voice,language='en')
        except sr.UnknownValueError:
            alixa("sorry i did not get that")
        except sr.RequestError:
            alixa("sorry Service is Down")
        return voice_data.lower()

def check(voice_data):
    if "name" in voice_data:
        alixa("Your name is Mohamed Ehab")
    if "time" in voice_data or "clock" in voice_data:
        alixa(ctime())
    if "search" in voice_data or "find" in voice_data:
        search = record("I think you mean this")

        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
    if "place" in voice_data or "location" in voice_data:
        location=record("I'll search for this place")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
    if "exit" in voice_data or "close" in voice_data:
        exit()

alixa ("Hi, How may i help you")
while True:
    data = record()
    check(data)