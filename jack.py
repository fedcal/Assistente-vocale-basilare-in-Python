# pip install pyttsx3
# pip install SpeechRecognition
# pip install pipwin
# pip install wikipedia
# pip install pyautogui
# pip install psutil
# pip install pyjokes

# pipwin install pyaudio

import pyttsx3 
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import os
import psutil 
import pyjokes

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    current_date=str(day)+"/"+str(month)+"/"+str(year)
    speak(current_date)

def wishme():
    speak("Benvenuto, sono Jack il tuo assistente personale")
    speak("Come posso aiutarti?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ti sto ascoltando...")
        r.pause_threshold= 3
        audio=r.listen(source)
    try:
        print("Riconoscendo l'input vocale....")
        query=r.recognize_google(audio, language='it-IT')
        print(query)
    except Exception as e:
        print(e)
        speak("Non ho capito bene ripeti perfavore...")
        return "None"
    return query

def sendemail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('1','2')#modificare il campo 1 con la mail e il campo 2 con la password
    server.sendmail('1',to,content)#inserire nel campo 1 la mail
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save('E:\Progetti Python\Assistente vocale')
def cpu():
    usage =str(psutil.cpu_percent()) 
    speak('CPU è al '+usage)
    battery= psutil.sensor_battery()
    speak('Il livello della batteria è: '+battery.percent())
def jokes():
    speak(pyjokes.get__joke())


if __name__=="__main__":
    wishme()
    while True:
        query= takeCommand().lower()
        if 'ora' in query:
            time()
        elif 'data' in query:
            date()
        elif 'wikipedia' in query:
            speak("Fammi controllare")
            query= query.replace("wikipedia","")
            result= wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("Qual'è il corpo della mail?")
                content= takeCommand()
                speak("A chi devo inviare la mail?")
                content2= takeCommand()
                sendemail(content2, content)
                speak("L'Email è stata inviata")
            except Exception as e:
                print(e)
                speak("Impossibilitato a inviare la mail")
        elif 'cerca su google' in query:
            speak("Cosa devo cercare?")
            chromepath= "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search= takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
        elif 'disconnetti'in query:
            os.system("shutdown -l")
        elif 'spegnimento'in query:
            os.system("shutdown /s /t l")
        elif 'riavvia'in query:
            os.system("shutdown /r /t-l")
        elif 'riproduci musica' in query:
            songs_dir='D:\\Musica' #Modificare questa riga con il path della cartella musica
            songs= os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'aggiungi promemoria' in query:
            speak("Quale promemoria ti devo ricordare?")
            data= takeCommand()
            speak("hai detto di ricordarti di: "+data)
            remember= open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'leggi promemoria' in query:
            remember=open('data.txt','r')
            speak('Avevi detto di ricordarti: '+remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak('Fatto')
        elif 'cpu' in query:
            cpu()
        elif 'racconta una barzelletta' in query:
            jokes()
        elif 'arrivederci' in query:
            quit()
     
