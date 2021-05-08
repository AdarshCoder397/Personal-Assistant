from os.path import join
from more_itertools.more import replace
import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pywhatkit
import pyautogui
import wolframalpha
import time

try:
    app = wolframalpha.Client("7A663R-XAU98QXA4Y")
except Exception:
    print("internet error")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):  # here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir i am virtual assistent Alexa")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir i am virtual assistent Alexa")
    else:
        speak("good evening sir i am virtual assistent Alexa")

# now convert audio to text

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognising...")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:  # For Error handling
        pass
        return "none"
    return text


def takecom2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        # print("Listening....")
        audio = r.listen(source)
    try:
        r.pause_threshold = 0.5
        # print("Recognising...")
        text = r.recognize_google(audio, language='en-in')
        # print(text)
    except Exception:  # For Error handling
        pass
        return "none"
    return text


# for main function
def TaskExcecution():
    while True:
        query = takecom().lower()
        if "wikipedia" in query:
            speak("searching details Wait")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'type' in query:
            query = query.replace("type", "")
            time.sleep(1)
            speak("writing sir")
            pyautogui.typewrite(query)
        elif 'music from pc' in query or "music" in query:
            speak("ok sir")
            music_dir = 'D:\\MUSIC'
            musics = os.listdir(music_dir)
            speak("which music sir")
            song = takecom().lower()
            if '52' in song:
                os.startfile(os.path.join(music_dir, musics[0]))
            elif 'aaja' in song:
                os.startfile(os.path.join(music_dir, music_dir[1]))
            elif 'devar' in song:
                os.startfile(os.path.join(music_dir, music_dir[2]))
            elif 'burj khalifa' in song:
                os.startfile(os.path.join(music_dir, music_dir[3]))
            elif 'butterfly' in song:
                os.startfile(os.path.join(music_dir, music_dir[4]))
            elif 'tera c' in song:
                os.startfile(os.path.join(music_dir, music_dir[5]))
            elif 'chori' in song:
                os.startfile(os.path.join(music_dir, music_dir[6]))
            elif 'firse' in song:
                os.startfile(os.path.join(music_dir, music_dir[7]))
            elif 'tori' in song:
                os.startfile(os.path.join(music_dir, music_dir[8]))
            elif 'ko' in song:
                os.startfile(os.path.join(music_dir, music_dir[9]))
            elif 'jigra' in song:
                os.startfile(os.path.join(music_dir, music_dir[10]))
            elif 'kamar' in song:
                os.startfile(os.path.join(music_dir, music_dir[11]))
            elif 'kh' in song:
                os.startfile(os.path.join(music_dir, music_dir[12]))
            elif 'pyaar' in song:
                os.startfile(os.path.join(music_dir, music_dir[13]))
            else:
                pywhatkit.playonyt(song)
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'Videos'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'good bye' in query:
            speak("Bye sir i am always here")
            # exit()
            break
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!',
                      'I am nice and full of energy', 'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information ADARSH KUMAR Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Alexa an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello Alexa" in query:
            hel = "Hello Adarsh Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Alexa"
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
        elif query == 'none':
            continue
        elif 'sleep' in query or 'abort' in query or 'stop' in query or 'sleep' in query or 'thanks' in query:
            ex_exit = 'ok sir you can call me anytime'
            speak(ex_exit)
            break
        elif 'open whatsapp' in query:
            speak("sure sir,opening whatsapp")
            webbrowser.open("https:\\web.whatsapp.com")
            speak("done sir")
        elif 'pycharm' in query:
            speak("opening pycharm")
            p_dir = "D:\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(os.path.join(p_dir))
        elif 'vs code' in query:
            speak("opening sir")
            v_dir = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(os.path.join(v_dir))
        elif 'bye' in query:
            speak("Bye sir;you can call me anytime")
            break
        elif 'text 3' in query:
            speak("opening subline text 3")
            s_dir = "D:\\Sublime Text 3\\sublime_text.exe"
            os.startfile(os.path.join(s_dir))
        elif 'notepad' in query:
            n_dir = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(os.path.join(n_dir))
        elif 'weather' in query:
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)
        elif 'create a note' in query:
            speak("What is the note sir")
            note = takecom()
            if(not os.path.exists("note.txt")):
                with open("note.txt", "w") as f:
                    f.write(note)
                    f.close()
            elif(os.path.exists("note.txt")):
                with open("note.txt", "w") as f:
                    f.write(note)
                    f.close()
        elif 'read note' in query:
            speak("wait sir")
            if(os.path.exists("note.txt")):
                with open("note.txt", "r") as f:
                    note = f.read()
                speak("sir the note is")
                speak(note)
                f.close()
            elif(not os.path.exists("note.txt")):
                with open("note.txt", "r") as f:
                    note = f.read()
                speak("sir the note is")
                speak(note)
                f.close()
        elif 'calculate' in query:
            try:
                speak("what sir")
                result = takecom().lower()
                res = app.query(result)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception as e:
                print(e)
                speak("I didn't")
                continue
        elif 'intellij' in query:
            i_dir = "D:\\IntelliJ IDEA Community Edition 2020.3.1\\bin\\idea64.exe"
            os.startfile(os.path.join(i_dir))
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif 'windows key' in query:
            pyautogui.keyDown("win")
            time.sleep(1)
            pyautogui.keyUp("win")
        elif 'alt' in query:
            pyautogui.keyDown("alt")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif 'igi' in query:
            pyautogui.keyDown("win")
            pyautogui.keyUp("win")
            pyautogui.click(200, 230)
        elif 'command prompt' in query:
            c_dir = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(os.path.join(c_dir))
        elif 'cutie' in query:
            q_dir = "D:\\qt designer\\designer.exe"
            os.startfile(os.path.join(q_dir))
    while True:
        query2 = takecom2().lower()
        if 'wake' or 'activate' in query2:
            rt = ['Ready sir', 'waked up sir', 'Sure sir']
            speak(random.choice(rt))
            TaskExcecution()
        elif 'quit' in query2:
            speak("goodbye sir")
            print("goodbye sir :)")
            exit()
        else:
            continue

if __name__ == "__main__":
    wish()
    TaskExcecution()
