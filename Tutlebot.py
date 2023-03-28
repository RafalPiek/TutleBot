import speech_recognition as sr
import fspeech as fs
r=sr.Recognizer()





# try:
def getText():
    with sr.Microphone() as source:
        try:
            # print("Słucham")
            audio=r.listen(source)
            text=r.recognize_google(audio,language='pl-PL')
            if text !='"':
                if "tutle bot" in text.lower():
                    text="słucham"
                return text
            return 0
        except:
            return 0
while True:
    txt=getText()
    # txt="bot"
    
    if not txt==0 and fs.wake_up(txt)==1: 
        while True:
            txt=getText()
            # txt="Wyłącz się"
            # txt=str(input("Podaj komende test:"))
            if not txt==0 and fs.stop_listen(txt)==0:

                print(txt)
                fs.mow(txt)
                break
            else:
                break
    else:
        pass
# except Exception as e:
#     print(e)
#     print("coś poszło nie tak")
# finally:
fs.engine.stop()