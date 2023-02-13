import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning Sir!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    
    else:
        speak("Good Evening Sir!")

    speak("I am Anasthesia. How may I help You?")


def takeCommand():
    #It takes microphone input from user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"

    return query





if __name__ == "__main__":
    wishMe()

    while True:
        query= takeCommand().lower()

        # logics for executing tasks based on query
        if "who am i" in query:
            speak("You are the most handsome man in this world.")

        elif "who are you" in query:
            speak("I am your assistant, Anasthesia.")

        elif "who is my girlfriend" in query:
            speak("If you want I can be your girlfriend.")

        elif "tell me your thoughts about me" in query:
            speak("The only thing i want to tell you is, I love You.")

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', '')
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")

        elif "play music" in query:
            # music_dir= "D:\\songs"
            # songs= os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))

            speak("You have no music file...")

        elif "this time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is: {strTime}")

        elif "brave browser" in query:
            openBrowser= "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(os.path.join(openBrowser))

        elif "open email" in query:
            webbrowser.open("gmail.com")

        

        elif "quit" in query:
            speak("Thanks sir for using me.")
            exit()
            



    