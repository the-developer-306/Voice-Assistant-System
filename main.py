import pyttsx3
import datetime
import speech_recognition as sr
import os
import mysql.connector
from pywikihow import search_wikihow
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)

database_variable = 0

def speak(audio):

    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning BOSS")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon BOSS")
    else:
        speak("Good evening BOSS")
    speak("greetings from JARVIS")


def database_connector():
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='', database="datatank")
    # print(mydb.connection_id)
    cs = mydb.cursor()  # cs cursor object
    # print(mydb.is_connected())
    speak("Connection successfull")
    #Jarvis_brain_gui.database()
    database_variable = 1

    speak("Sir your personal database is now online. Please tell me whether you have to fetch or feed data in your database ?")
    feed_fetch_choice = takeCommand()
    
    if feed_fetch_choice.lower() == "i have to feed data":
        speak("Sir what exactly you have to feed")
        u = takeCommand()

        if u.lower() == "jarvis add a new contact":

            speak("Sir please tell the name of the person")
            nm = takeCommand()
            speak("Sir please tell the surname of that person")
            srnm = takeCommand()
            speak("Sir please tell the mobile number of that person")
            mn = takeCommand()
            speak("Sir please tell the bio of that person")
            bio = takeCommand()

            st = "insert into contacts(NAME , SURNAME , MOBILE_NUMBER , bio) values(%s,%s,%s,%s)"
            value = (nm, srnm, mn, bio)
            cs.execute(st, value)
            mydb.commit()
            speak("Sir your data has been entered...")
                

    # if feed_fetch_choice.lower() == "i have to fetch data":
    #     speak("Sir please tell from which table you have to fetch data. Please choose one from below...")
    #     print("1). Contacts list                              2). Location log table")
    #     speak("Contacts list or location log table")
    #     u = takeCommand()
    #     # if u.lower() = "contacts list":

    #     # if u.lower() = "location log table":

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        r.energy_threshold = 800  # minimum audio energy to consider for recording
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        speak("Sir, I am not able to recognise what you said. Say that again please...")
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


def executer():

    speak("Initialising the engines, initiating the processing units, connecting to the artificial intelligence databases, setting up the environment variables, creating storage units")
    speak("All initialisations done... virtual memory created")
    speak("Welcome Sir. I am Jarvis, online and ready to assist you.")
    wishme()
    # this function performs various commands given by the user
    while True:
        userinput = takeCommand()
        if userinput.lower() == "ok jarvis go to sleep":
            speak(
                "Shutting down the artificial intelligence databases... shutting down the processing units...  shutting down engines... have a nice day BOSS !!!")
            exit()

        if userinput.lower() == "jarvis open google chrome":
            speak("Sir opening google chrome")
            webbrowser.open("https://google.com")
                
        if userinput.lower() == "jarvis trigger zoom":
            speak("Sir opening your zoom application")
            zoom = ''
            os.startfile(os.path.join(zoom))

        if userinput.lower() == "jarvis check my telegram":
            speak("Sir checking your telegram")
            tele = ''
            os.startfile(os.path.join(tele))

        if userinput.lower() == "jarvis connect to my database":
            speak("Sir connecting to your database")
            database_connector()

        if userinput.lower() == "jarvis activate method mode" :
            speak("Sir method mode is activated.")
            while True:
                speak("Please tell me what do you want to know")
                how = takeCommand()
                try:
                    if "ok jarvis exit method mode" in how.lower() :
                        speak("As you wish sir..... closing method mode..... method mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir, I am not able to answer this at the current moment")

        if userinput.lower() == "jarvis activate search mode":
            speak("Sir search mode is activated")
            while True:
                speak("Please tell me what do you want to search")
                ques = takeCommand()
                if "ok jarvis exit search mode" in ques.lower() :
                        speak("As you wish sir..... closing search mode..... search mode is closed")
                        break
                else:
                    webbrowser.open("https://google.com/search?q="+ques)
