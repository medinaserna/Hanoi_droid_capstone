# for me, before use speech package i should done this:
#pip install pipwin 
#pipwin install pyaudio

import serial
import speech_recognition as sr

have_a_command = False

mic = sr.Microphone()
sr.Microphone.list_microphone_names()

mic = sr.Microphone(device_index=2)  # microphone high definition

# Initialize the recognizer
recognizer = sr.Recognizer()

def start_robot_voice_command():
    try:
        with mic as source:
            print("Listening for 'robot start' command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            have_a_command = True
        command = recognizer.recognize_google(audio).lower()
        
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        have_a_command = False
        command = False
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        have_a_command = False
        command = False
        
    return have_a_command, command
        