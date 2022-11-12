import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Sir, I am Jarvis, I am at your command")


def command_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Say that again please.......")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        query = command_user().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedida.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Sir, According to Wikipedia")
            speak(results)

        elif "open my youtube channel" in query:
            speak("Opening your Youtube Channel, Sir")
            webbrowser.get(chrome_path).open("https://www.youtube.com/channel/UC__X83ubVHsG8t0-Y569qNw")

        elif "open youtube" in query:
            speak("Opening YouTube.......")
            webbrowser.get(chrome_path).open("youtube.com")

        elif "open google" in query:
            speak("Opening Google.......")
            webbrowser.get(chrome_path).open("google.com")
        
        elif "open twitter" in query:
            speak("Opening Twitter.......")
            webbrowser.get(chrome_path).open("twitter.com")

        elif "open facebook" in query:
            speak("Opening Facebook.......")
            webbrowser.get(chrome_path).open("facebook.com")
        
        elif "open insta" in query:
            speak("Opening Instagram.......")
            webbrowser.get(chrome_path).open("instagram.com")

        elif "what time is it now" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, right now the time is {strTime}")
        
        elif "mi pro" in query:
            speak("Sir, you are super ultra limited edition pro")
            speak("Sir, and one more thing your little sister is super ultra mega limited edition noob")

        # Songs&Music Parts
        elif "play strawberry" in query:
            webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=Mw5mAozjC6M")
            speak("Playing")
        elif "play astronaut" in query:
            speak("Playing")
            webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=c6ASQOwKkhk")
        