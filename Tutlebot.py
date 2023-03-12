
import speech_recognition as sr
import tutlesql as tsq
import fspeech as fs
r=sr.Recognizer()



tsq.create_table()
try:
    
        

    def getText():
        with sr.Microphone() as source:
            try:
                print("Listening...")
                audio=r.listen(source)
                text=r.recognize_google(audio,language='pl-PL')
                if text !='"':
                    return text
                return 0
            except:
                return 0
    while True:
        # txt=getText()
        txt="wiki youtube"
        
        if not txt==0:
            # txt="czym jesteś"
            print(txt)
            fs.mow(txt)
            break
        else:
            print("nie udało się rozpoznać...")
            continue
except Exception as e:
    print(e)
    print("coś poszło nie tak")
finally:
    fs.engine.stop()