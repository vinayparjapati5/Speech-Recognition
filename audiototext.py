import speech_recognition as sr

def main():
    r= sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold=0.6

        audio = r.listen(source)

        try:
            ask = r.recognize_google(audio, language='en-us')
            print(f"Converted Audio is: {ask}" )

        except Exception:
                print("say that again")
                return ""

    return ask

main()