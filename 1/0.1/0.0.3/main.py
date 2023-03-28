import speech_recognition as sr
import conversation1
import pyttsx3
import openApplication


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=6)
        said = ""
        # try:
        s = r.recognize_google(audio)
        said = s.lower()
        reply(said)
        # except Exception as e:
        #   print("Exception: " + str(e))
    return None


def reply(said):
    engine = pyttsx3.init()  # speaking function initiated
    rep = ""
    if "open" in said:
        openApplication.openCommand(said)
    elif "search" in said:
        openApplication.searchOnline(said)
    elif "terminate" in said:
        print("Terminating the session")
        exit()
    else:
        rep = conversation1.savedReply(said)
        print(rep)
    engine.say(rep)
    print("Speaking")
    engine.runAndWait()
    get_audio()


get_audio()
