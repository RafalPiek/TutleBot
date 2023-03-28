from pywttr import Wttr
import os
import pyttsx3 as tts
import wikipediaapi 
import sys

wiki_wiki=wikipediaapi.Wikipedia('pl')
engine=tts.init()
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# sys.exit()
def mow(text):

        if "pogoda" in text.lower() or "pogoda w" in text.lower():
            # text_table=text.split(' ')
            # text=text_table[0]
            tab_pogoda=['w','pogoda','jutro','pojutrze']
            
            text_table=text.split(' ')
            for i in tab_pogoda:
                try:
                    text_table=text_table[text_table.index(i)+1:]
                    break
                except:
                    pass
            
            try:      
                wttr=Wttr(text_table)
                forecas=wttr.pl()
                if "jutro" in text.lower():
                    

                    temp=forecas.weather[1].hourly[0].temp_c
                    temp=str(temp)
                    sky=forecas.weather[1].hourly[0].lang_pl[0].value
                    text=text +", będzie "+ temp+" stopni celcjusza oraz "+sky
                elif "pojutrze" in text.lower():
                    temp=forecas.weather[2].hourly[0].temp_c
                    temp=str(temp)
                    sky=forecas.weather[2].hourly[0].lang_pl[0].value
                    text=text +", będzie "+ temp+" stopni celcjusza oraz "+sky
         
                else:
                    temp=forecas.current_condition[0].temp_c
                    temp=str(temp)
                    sky=forecas.current_condition[0].lang_pl[0].value
                    text="Teraz "+ text +", jest "+ temp+" stopni celcjusza oraz "+sky

                print(text)
            except:
                text="nie znaleziono takiego miasta"
            
            
        elif "kto cie stworzył" in text.lower() or "czym jesteś" in text.lower() or "przedstaw się" in text.lower():
            text="Jestem TUTELBOT, czyli prostym programem wykorzystującym kilka bliblotek, zostałem stworzony przez RP"



        elif "otwórz przeglądarkę"==text.lower():
            text=''
            os.system("start \"\" https://www.google.com")



        elif "otwórz yt"==text.lower() or "otwórz youtube"==text.lower():
            text=''
            os.system("start \"\" https://www.youtube.com") 



        elif "otwórz w yt" in text.lower() or "otwórz w youtube" in text.lower() or "otwórz w youtubie" in text.lower():
            tab_yt=['yt','youtube','youtubie']
            text_table=text.split(' ')
            for i in tab_yt:
                try:
                    text_table=text_table[text_table.index(i)+1:]
                    break
                except:
                    pass

            text='+'.join(text_table)
            website="start \"\" https://www.youtube.com/results?search_query="+text
            print(website)
            os.system(website) 
            text="Otwieram youtube"


        elif text=="Wyłącz się":
            text="Wyłączam się"
            # os.system("shutdown /s /t 1")
            sys.exit()




        elif "znajdż" in text.lower() or "wyszukaj" in text.lower():
            text_table=text.split(' ')
            tab_search=['znajdz','wyszukaj']
            for i in tab_search:
                try:
                    text_table=text_table[text_table.index(i)+1:]
                    break
                except:
                    pass
            text='+'.join(text_table)
            website="start \"\" https://www.google.pl/search?q="+text
            os.system(website)
        elif "wikipedia" in text.lower() or "wiki" in text.lower() or "co to znaczy" in text.lower():
            wiki_wiki=wikipediaapi.Wikipedia('pl')
            text_table=text.split(' ')
            tab_search=['wikipedia','wiki','znaczy']
            for i in tab_search:
                try:
                    text_table=text_table[text_table.index(i)+1:]
                    break
                except:
                    pass
            text='+'.join(text_table)
            
            
            page_wiki=wiki_wiki.page(text)  
            if page_wiki.exists():
                
                text="Jak podaje wykipedia",page_wiki.summary

            else:
                website="start \"\" https://pl.wikipedia.org/wiki/Special:Search?search="+text
                # website="start \"\" https://en.wikipedia.org/wiki/"+text
                os.system(website)
        elif "słucham" in text.lower():
            text="Tak słucham"
        else:
            text="Nie dosłyszałem, czy mógłbyś powtórzyć?"

        engine.say(text)
        engine.runAndWait()
def wake_up(text):
    if "bot" in text.lower():
        text="Słucham"
        engine.say(text)
        engine.runAndWait()
        return 1
    else:
        return 0
def stop_listen(text):
    if "stop" == text.lower():
        text="Dobrze przestaje słuchać"
        engine.say(text)
        engine.runAndWait()
        return 1
    else:
        return 0