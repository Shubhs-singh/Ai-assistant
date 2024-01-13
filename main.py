import os 
import pygame
import speech_recognition as sr

def speak(text):
    voice ="en-US-AriaNeural"
    
    command= f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    
    os.system(command)
    pygame.mixer.init()
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("output.mp3")
        
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing .....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print('Recognizing')
        query = r.recognize_google(audio, language ='en-us')
    except Exception as e:
        print(e)
        return ''
    return query
speak(" hello how are you shubham you are great")
query = take_command()
print(query)

while True:
    query = take_command()
    print("You:" + query)
    if ' hello' in query or 'hey' in query:
        speak("hi how are you")
    elif ' i am fine ' in query:
        speak('thats great to hear')
    else :
        speak(' i dont understand ') 
    