import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    except Exception as e:
        print(f"Error recognizing speech: {e}")
        return "None"
    
    return query


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password-here')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send the email")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what is menstrual cycle' in query:
            speak("The menstrual cycle is a natural process. It is a complex cycle controlled by female hormones that cause regular bleeding (periods). The menstrual cycle has four phases: menstruation, the follicular phase, ovulation and the luteal phase. Some women may experience menstrual problems")
            break

            
        elif 'how long does a normal menstrual cycle last' in query:
            speak("The average menstrual cycle lasts 28 days. However, cycles lasting as little as 21 days or as long as 35 days can be normal.")
            break


        elif 'different phases of the menstrual cycle' in query:
            speak("The four phases of the menstrual cycle are menstruation, the follicular phase, ovulation and the luteal phase")
            break


        elif 'what is ovulation and when does it occur' in query:
            speak("Ovulation is a phase of the female menstrual cycle that involves the release of an egg (ovum) from one of the ovaries. It generally occurs about two weeks before the start of the menstrual period.")
            break


        elif 'what is a normal period' in query:
            speak("The average menstrual cycle is about 25-30 days, but it can be as short as 21 days or longer than 35 — it's different from person to person.")
            break


        elif 'what is pcos' in query:
            speak("Polycystic ovaries, hormone imbalance and irregular periods are telltale signs and symptoms of polycystic ovary syndrome")
            break


        elif 'what is pms' in query:
            speak("Premenstrual syndrome (PMS) is when a girl has mood and body changes before or during her period. It's usually at its worst during the 4 days before a period. PMS usually goes away 2 to 3 days after the period begins")
            break


        elif 'what are symptoms of pms' in query:
            speak("mood swings, feeling down or anxious, feeling irritable, feeling bloated – your tummy sticks out more than normal, headaches, breast tenderness or changes, changes in skin (like spots or dryness)")
            break


        elif 'symptoms of pcod' in query:
            speak("missed or irregular menstrual periods, excess hair growth, acne, infertility, and weight gain.")
            break

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break