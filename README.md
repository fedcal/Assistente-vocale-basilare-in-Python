# Assistente-vocale-basilare-in-Python
Assistente vocale basilare in Python

Questo progetto nasce con l'intenzione di rendere open source i miei progetti per facilitare chi si avvicina 
per la prima volta al mondo della programmazione. In questo progetto si sviluppa un piccolo assistente 
vocale in Python, con funzioni basilari che andrò successivamente ad ampliare. Per adesso, in questo progetto,
questo assistente vocale potrà:
- mandare mail
- prendere nota di un promemoria alla volta (successivamente verrà ampliato per più promemoria)
- leggere il promemoria (anche questa funzionalità verrà ampliata successivamente)
- mandare mail
- effettuare ricerche su Google e Wikipedia
- vedere lo stato della CPU e della batteria
- esprimere data e ora corrente
- raccontare barzellette

Come provare il software

Innanzitutto dovete scaricare python sul proprio dispositivo andando sul sito https://www.python.org/downloads/
e scegliere l'eseguibile del linguaggio. Successivamente dovete aprire il cmd del vostro sistema e scaricare
le seguenti librireri python indispensabili per il buon funzionamento del programma:
- pip install pyttsx3
- pip install SpeechRecognition
- pip install pipwin
- pip install wikipedia
- pip install pyautogui
- pip install psutil
- pip install pyjokes
- pipwin install pyaudio

Una volta fatto ciò potete creare un progetto con un IDE (si consiglia Visual Stuio Code o PyCharm) in cui
includere il main e poi eseguirlo.
Fate molta attenzione. Dovete modificare le righe numero 62 e 63 con le informazioni necessarie per poter 
inviare le mail.
