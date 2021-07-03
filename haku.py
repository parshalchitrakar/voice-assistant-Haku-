import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()#alert to machine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hi i am your personal assistant ")
engine.say("please order saying hello ")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

    
def take_command():
    try:# check if listener is there or not. when try comes then except will come.
        with sr.Microphone() as source:
            print("Listining.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello'  in command:
                command = command.replace('hello','')
                
    except:
        pass
    return command

def PA_run():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk("Playing ....." + song )
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is '+ time)
        print(time)
    elif 'who is ' or 'tell me' or 'search ' in command:
        person = command.replace('Who is ','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say the command again.")
while True:
    PA_run()

