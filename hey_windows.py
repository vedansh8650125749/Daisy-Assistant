import pyttsx3   #text-to-speech conversion
import datetime     #use to fetch current datetime
import speech_recognition as sr     #use to reconize speech to text
import wikipedia         #use to search breifly
import webbrowser        #use to open web with search
import os                #use to open and fetch directories
import subprocess        #use for handle process in run in background
import pyjokes           #use for tell jokes 
import ctypes            #handle c data types
import time              #fetching local time
import winshell          #handle system apps
import pywhatkit as pwk  #use to interact different apps
import pyautogui
import wolframalpha      #use to get expert level answers
from dotenv import load_dotenv  #used to fetch env files
import requests
from twilio.rest import Client
import newsapi
from newsapi import NewsApiClient
import pystray
from PIL import Image
from threading import Thread
import multiprocessing as mp
import sys
import logging



logging.basicConfig(filename='Daisy.log',level=logging.INFO,format='%(asctime)s %(levelname)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')


def configure():
    load_dotenv() 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voice_rate = 190
engine.setProperty('rate', voice_rate)  #decrease rate of speak

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour < 12:
        print(f'Good morning dear, its {tt}')
        speak(f'Good morning dear, its {tt}')
    elif hour >= 12  and hour <18:
        print(f'Good Afternoon dear, its {tt}')
        speak(f'Good AfterNoon dear, its {tt}')
    else:
        print(f'Good Evening dear, its {tt}')
        speak(f'Good Evening dear, its {tt}')     

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening !....')
        r.energy_threshold = 500 #voice cancellation
        r.pause_threshold = 0.5 #resopnse delay
        r.dynamic_energy_adjustment_damping = 0.1
        r.dynamic_energy_ratio = 0.3
        audio = r.listen(source)   

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        logging.info(f'User said: {query}')

    except Exception as e:
        #print(e)
        print('Can you say it Agian......')
        logging.warning(f'Error recognizing user input: {e}')
        return "None"
    return query


def news():
    News_API =  os.getenv('news_api') 
    main_url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={News_API}'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth']
    for ar in articles:
        head.append(ar['title'])
        
    for i in range(len(day)):
        print(f'todays {day[i]} news is: {head[i]}')
        speak(f'todays {day[i]} news is: {head[i]}')   

def cat_news(category):
    if category == "sports":
        try:
            headlines = newsapi.get_top_headlines(country='in', category='sports')
            head = []
            day = ['first', 'second', 'third']

            for ar in headlines['articles']:
                head.append(ar['title'])

            speak('wait i ll fetching')
            for i in range(len(day)):
                print(f'todays {day[i]} sports news is: {head[i]}')
                speak(f'todays {day[i]} sports news is: {head[i]}')
        except:
            headlines = newsapi.get_top_headlines(country='us', category='sports')
            head = []
            day = ['first', 'second', 'third']

            for ar in headlines['articles']:
                head.append(ar['title'])

            speak('wait i ll fetching')
            for i in range(len(day)):
                print(f'todays {day[i]} sports news is: {head[i]}')
                speak(f'todays {day[i]} sports news is: {head[i]}')        
                      

    elif category == "business":
        try:
            headlines = newsapi.get_top_headlines(country='in', category='business')
            head = []
            day = ['first', 'second', 'third']

            for ar in headlines['articles']:
                head.append(ar['title'])

            speak('wait i ll fetching')
            for i in range(len(day)):
                print(f'todays {day[i]} business news is: {head[i]}')
                speak(f'todays {day[i]} business news is: {head[i]}')
        except:
            headlines = newsapi.get_top_headlines(country='us', category='business')
            head = []
            day = ['first', 'second', 'third']

            for ar in headlines['articles']:
                head.append(ar['title'])

            speak('wait i ll fetching')
            for i in range(len(day)):
                print(f'todays {day[i]} business news is: {head[i]}')
                speak(f'todays {day[i]} business news is: {head[i]}')        

    elif category == "technology":
        headlines = newsapi.get_top_headlines(country='us', category='technology')
        head = []
        day = ['first', 'second', 'third']

        for ar in headlines['articles']:
            head.append(ar['title'])

        speak('wait i ll fetching')
        for i in range(len(day)):
            print(f'todays {day[i]} tech news is: {head[i]}')
            speak(f'todays {day[i]} tech news is: {head[i]}')

    elif category == "science":
        headlines = newsapi.get_top_headlines(country='us', category='science')
        head = []
        day = ['first', 'second', 'third']

        for ar in headlines['articles']:
            head.append(ar['title'])

        speak('wait i ll fetching')
        for i in range(len(day)):
            print(f'todays {day[i]} news is: {head[i]}')
            speak(f'todays {day[i]} news is: {head[i]}')

    elif category == "health":
        try:
            headlines = newsapi.get_top_headlines(country='in', category='health')
            head = []
            day = ['first', 'second', 'third']

            for ar in headlines['articles']:
                head.append(ar['title'])

            speak('wait i ll fetching')
            for i in range(len(day)):
                print(f'todays {day[i]} news is: {head[i]}')
                speak(f'todays {day[i]} news is: {head[i]}')    
        except:
            headlines = newsapi.get_top_headlines(country='us', category='health')
            head = []
            day = ['first', 'second', 'third']

            for ar in headlines['articles']:
                head.append(ar['title'])

            speak('wait i ll fetching')
            for i in range(len(day)):
                print(f'todays {day[i]} news is: {head[i]}')
                speak(f'todays {day[i]} news is: {head[i]}')        

    else:
        speak("Invalid category.")   
        print('Invalid Category')  

def check_for_reply():
    while True:
        time.sleep(2)
        if pyautogui.pixelMatchesColor(700, 700, (255, 255, 255)):
            print("New message received!")
            speak("You have a new message on WhatsApp.")
        break    

def send_whatsapp_message(number, message):
    pwk.sendwhatmsg_instantly(f"+91{number}", message)

def callback():
    try:
        os.system("taskkill /f /im WindowsTerminal.exe")
    except:
        pyautogui.hotkey('shift', 'f5')    
        
def setup_system_tray():
    try:
        image = Image.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\icon\\voice.png") # replace with your icon's path
        menu = pystray.Menu( pystray.MenuItem("Exit", callback) )
        tray_icon = pystray.Icon("name", image, "Daisy", menu)
        tray_icon.run()
    except Exception as e:
        image = Image.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\icon\\voice_danger.png") # replace with your icon's path
        tray_icon = pystray.Icon("name", image, "Daisy")
        tray_icon.run()    

def ico():
    thread = Thread(target=setup_system_tray)
    thread.start()


if __name__ == "__main__":

    if 1:
        configure()
        clear = lambda: os.system('cls')
        clear()
        ico()
        wishMe()
        speak("Hi i m Daisy. How can i help you")
    # Start the process to check for new replies
    process = mp.Process(target=check_for_reply)
    process.start()
    #-------------------------------------------------------------------------------------Starts Here------------------------------------------------------------------------

    while True:
    #if 1:  
        logging.info('Daisy: ')
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak("According to Wikipedia")
            speak(results)

        elif 'play' in query:
            song = query.replace('play','')
            speak('Alright dear, ill shuffle the music playing in youtube')
            pwk.playonyt(song)

        elif 'open chat gpt' in query:
            speak('opening Chat gpt')
            webbrowser.open('https://chat.openai.com/chat')

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')


        elif 'open google' in query:
            speak('opening google')
            speak('dear, what should i search for you')
            cmd = takeCommand()
            webbrowser.open(f'{cmd}')

        elif 'the time' in query:
            dt = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Dear, the time is {dt}") 

        elif 'play music' in query:
            speak('opening dear')
            webbrowser.open('youtube.com/music')    

        elif 'open visual studio' in query:
            speak('opening microsoft visual studio code')
            path1 = "C:\\Users\\vedan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path1) 

        elif 'open a website' in query:
            query = query.replace('open a website', '')
            speak('sure dear tell me the name') 
            web_input = takeCommand()
            webbrowser.open(f'https://www.bing.com/search?q={web_input}')

        elif 'search a website' in query: 
            query = query.replace('search a website', '')
            speak('sure dear tell me the name') 
            web_input = takeCommand()
            webbrowser.open(f'https://www.bing.com/search?q={web_input}')         

        elif 'open gmail' in query:
            speak('opening gmail in web')
            webbrowser.open('gmail.com')

        #system programs    ------------------------------------------------------------------------------------------
        #opening --------------------------------------------

        elif "log off my device" in query or "sign out my device" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"]) 

        elif 'lock my screen' in query or 'lock my window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'lock my device' in query or 'lock my system' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()        
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "open notepad" in query:
            speak('opening notepad') 
            os.system("start notepad")

        elif "open command prompt" in query or "open cmd" in query:
            speak('opening command prompt') 
            os.system("start cmd")

        elif 'open spotify' in query:
            speak('opening spotify')
            path = "C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.195.893.0_x86__zpdnekdrzrea0\Spotify.exe"
            os.startfile(path)

        elif 'open team viewer' in query:
            speak('opening')
            path = "C:\Program Files\TeamViewer\TeamViewer.exe"
            os.startfile(path)    

        elif 'open calculator' in query:
            speak('opening calculator')
            path = "C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2208.1.0_x64__8wekyb3d8bbwe\CalculatorApp.exe"
            os.startfile(path)  
            
        elif 'open bluetooth' in query:
            speak('Click on bluetooth, dear')
            pyautogui.hotkey('winleft', 'a') 

        elif 'open wi-fi' in query:
            speak('Click on wifi, dear')
            pyautogui.hotkey('winleft', 'a')       

        #closing system applications------------------------------------------------------------------------------------------------------------

        elif "close the command prompt" in query or "close command prompt" in query:
            speak('ok dear, closing command prompt')
            os.system("taskkill /f /im OpenConsole.exe")   

        elif "close the notepad" in query or "close notepad" in query:
            speak('ok dear, closing notepad')
            os.system("taskkill /f /im notepad.exe") 

        elif "close the brave" in query or 'close brave' in query:
            speak('ok dear, closing brave')
            os.system("taskkill /f /im brave.exe") 

        elif 'close the edge' in query or 'close edge' in query:
            speak('ok dear, closing Microsoft Edge')
            os.system("taskkill /f /im msedge.exe") 

        elif 'close the chrome' in query or 'close chrome' in query:
            speak('ok dear, closing Microsoft Edge')
            os.system("taskkill /f /im chrome.exe") 

        elif 'close the firefox' in query or 'close firefox' in query:
            speak('ok dear, closing Microsoft Edge')
            os.system("taskkill /f /im firefox.exe") 

        elif 'close the opera' in query or 'close opera' in query:
            speak('ok dear, closing Microsoft Edge')
            os.system("taskkill /f /im opera.exe")   

        elif 'close the spotify' in query or 'close spotify' in query:
            speak('ok dear, closing spotify')
            os.system("taskkill /f /im Spotify.exe")      

        elif 'close the team viewer' in query or 'close team viewer' in query:
            speak('ok dear, closing team viewer')
            os.system("taskkill /f /im TeamViewer.exe")    

        elif 'close the task manager' in query or 'close task manager' in query:
            speak('ok dear, closing task manager')
            os.system("taskkill /f /im Taskmgr.exe")   

        elif 'close the calculator' in query or 'close calculator' in query:
            speak('ok dear, closing calculator')
            os.system("taskkill /f /im CalculatorApp.exe")             

        elif 'close bluetooth' in query:
            speak('Click on bluetooth, dear')
            pyautogui.hotkey('winleft', 'a')

        elif 'close wi-fi' in query:
            speak('Click on wifi, dear')
            pyautogui.hotkey('winleft', 'a')    

        #Searching---------------------------------------------------------------------------------------------------------  

        elif 'find' in query:
            query = query.replace('find', '')
            webbrowser.open(f'https://www.google.com/maps/search/{query}')

        elif 'what is the stock price of' in query:
            query2 = query.replace('what is the stock price of', '')
            results = webbrowser.open(query2 + ' stock Price')
            speak('here are some results !')

        elif 'show some stock price of' in query:
            query2 = query.replace('show some stock price of', '')
            results = webbrowser.open(query2 + ' stock Price')
            speak('here are some results !')

        elif 'tell me the stock price of' in query:
            query2 = query.replace('show some stock price of', '')
            results = webbrowser.open(query2 + ' stock Price')
            speak('here are some results !')    

        elif 'show me some todays stock market' in query:
            query2 = query.replace('show some stock price of', '')
            results = webbrowser.open(query2 + ' stock Price')
            speak('here are some results !') 

        elif "tell me today's stock price" in query:
            speak('which one dear')
            input1 = takeCommand()
            webbrowser.open(f"{input1} stock price") 
            speak('here are some results')                

        elif 'search' in query:
            query = query.replace('search', '')
            results = webbrowser.open(query)
            speak('here are some results !')

        elif 'can you suggest some music for' in query:
            speak('ofcourse dear')
            query.replace('can you suggest some music for', '')
            webbrowser.open('https://music.youtube.com/')
            speak('here are some results !')        

        elif 'show me' in query:
            query2 = query.replace('show me', '')
            results = webbrowser.open(query2)
            speak('here are some results !')  

        elif 'which' in query:
            query2 = query.replace('which', '')
            results = webbrowser.open(query2)
            speak('here are some results !')    

        elif 'who' in query:
            query2 = query.replace('who', '')
            results = webbrowser.open(query2)
            speak('here are some results !')    

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Locating" + location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "")

        #Reports  ---------------------------------------------------------------------------------------------------------------------------

        elif 'weather info' in query or 'weather information' in query:
            speak('tell me your area dear')
            location = takeCommand()
            speak('please wait while i fetching weather info dear')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv('weather_api')}"

            # HTTP request
            response = requests.get(url)
            if response.status_code == 200:
                data  = response.json()
                main = data['main']
                temperature = main['temp']
                celcius = round((temperature - 273.15), 2)
                humidity = main['humidity']
                pressure = main['pressure']


                # weather report
                report = data['weather']
                speak(f"Cureently weather of {location} is")
                print(f'-----------------{location}-----------------')

                speak(f"Current Temperature: {celcius} degree celcius")
                print(f'Temperature: {celcius}°C')

                speak(f"Humidity: {humidity}")
                print(f'Humidity: {humidity}%')

                speak(f"Pressure: {pressure}")
                print(f'Pressure: {pressure} Pa')

                speak(f"Today is: {report[0]['description']} day") 
                print(f"Day: {report[0]['description']}") 

        elif 'weather forecast in' in query:
            query3 = query.replace('what is the weather forecast in', '')
            location3 = query3
            speak("Feteching weather information of" + location3)
            webbrowser.open("https://www.msn.com/en-in/weather/forecast/in-" + location3 + ",India") 
            speak('here are some results')

        elif 'what is the weather for' in query:
            query3 = query.replace('what is the weather for', '')
            location3 = query3
            speak("Feteching weather information of" + location3)
            webbrowser.open("https://www.msn.com/en-in/weather/forecast/in-" + location3 + ",India") 
            speak('here are some results')

        #News  -------------------------------------------------------------------------------------------------------------------        

        elif 'tell me some news' in query or  "tell me some today's news" in query:
            api = os.getenv('news_api')
            newsapi = NewsApiClient(api_key=api)
            speak('dear which country you would like to hear news india or international')
            country = takeCommand().lower()
            if country == 'india':
                try:
                    headlines = newsapi.get_top_headlines(country='in')
                    head = []
                    day = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
                    for ar in headlines['articles']:
                        head.append(ar['title'])
                        
                    speak('Wait i ll fetching the news')    
                    for i in range(len(day)):
                        print(f'todays {day[i]} news is: {head[i]}')
                        speak(f'todays {day[i]} news is: {head[i]}')

                except Exception as e:

                    speak('Sorry dear I m unable to fetch news of india, would you like to hear some other news')
                    input1 = takeCommand().lower()

                    if input1 == 'yes' or input1 == 'ok':

                        speak('ok dear give some seconds')
                        headlines = newsapi.get_top_headlines(country='us')
                        head = []
                        day = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

                        for ar in headlines['articles']:
                            head.append(ar['title'])
                            
                        speak('Wait i ll fetching the news')    
                        for i in range(len(day)):
                            print(f'todays {day[i]} news is: {head[i]}')
                            speak(f'todays {day[i]} news is: {head[i]}')        
            else: 
                headlines = newsapi.get_top_headlines(country='us')
                head = []
                day = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
                for ar in headlines['articles']:
                    head.append(ar['title'])
                    
                speak('Wait i ll fetching the news')    
                for i in range(len(day)):
                    print(f'todays {day[i]} news is: {head[i]}')
                    speak(f'todays {day[i]} news is: {head[i]}')       


            speak("What type of news would you like to hear? Sports, Business, technology, health, science or Entertainment? ")
            print("What type of news would you like to hear? Sports, Business, or Entertainment? ")

            category = takeCommand().lower()
            cat_news(category)
                
        elif "show me some today's news" in query:
            query = query.replace("show me some today's news", "")
            results3 = webbrowser.open('news.google.com')
            speak('here are some news dear!')      

        elif 'show me some news of' in query :
            query3 = query.replace('tell me some news of', '')
            location3 = query3
            speak("Feteching news information of" + location3)
            webbrowser.open("https://www.google.com/search?q=" + location3 + ",+news") 
            speak('here are some results')   

        elif 'tell me some news of' in query :
            query3 = query.replace('tell me some news of', '')
            location3 = query3
            speak("Feteching news information of" + location3)
            webbrowser.open("https://www.google.com/search?q=" + location3 + ",+news") 
            speak('here are some results') 

        elif 'tell me the news of' in query:
            query3 = query.replace('tell me the news of', '')
            location3 = query3
            speak("Feteching news information of" + location3)
            webbrowser.open("https://www.google.com/search?q=" + location3 + ",+news") 
            speak('here are some results')

        elif 'news bulletins' in query:
            speak('please wait dear while i fetching news for you')
            news()        

        #Fun with Assistant  ---------------------------------------------------------------------------------------------------------

        elif 'what is your name' in query or 'who are you' in query :
            speak('I am daisy your AI designed voice assistant version 1.0 ')  

        elif 'i love you' in query:
            speak('i cant feel romantic love but i think you are wonderful ⭐')  

        elif 'say you love me' in query:
            speak('ok, i love you 💞') 

        elif 'shut up' in query:
            speak('ok ok dear cool down! relax')    

        elif 'very good' in query:
            speak('thanks dear')  

        elif 'well done' in query:
            speak("Ahh i'm happy you're happy 😊")       

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak('sorry i didnt catch your name')
            cmnd = takeCommand()
            try:
                if "it's" in cmnd:
                    cmnd = cmnd.replace("it's","")
                    speak(f"hi {cmnd}, How are you!")
                else:
                    pass
            except:
                pass    

        elif "who made you" in query or "who created you" in query:
            speak("sorry dear i cannot say.")

        elif "who i am" in query or "who am i" in query:
            speak("If you talk then definitely your human.")   
 
        elif "why you came to world" in query:
            speak("It's a secret dear")        
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine") 

        elif 'why you are so funny' in query:
            speak('so that i can make laugh to you dear')    

        elif 'did you marry with my brother' in query:
            speak("as i am your AI assistant i cant do such things dear.") 

        elif 'made you'in query or 'create you' in query:
            speak('At first i was an idea, then two people put head together. And came up with me') 

        elif 'hi' in query or 'hello' in query:
            speak('hello, how are you')   

        elif 'se' in query:
            query = query.replace('se','')
            speak(f'{query}')          
                 
        elif 'exit' in query or 'quit' in query:
            speak("Thanks dear for giving me your time")
            os.system("taskkill /f /im WindowsTerminal.exe")
            process.terminate()
            sys.exit() 
            
        elif 'jokes' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())      

        #ott platform   --------------------------------------------------------------------------------------------------------------------------

        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
            speak('opening netflix')

        elif 'open amazon prime' in query:
            webbrowser.open('primevedio.com')
            speak('opening Amazon Prime Vedio')        

        elif 'open zee five ' in query:
            webbrowser.open('zee5.com')
            speak('opening amazon')

        elif 'open voot' in query:
            webbrowser.open('voot.com')
            speak('opening amazon') 

        elif 'open disney plus hotstar' in query:
            webbrowser.open('hotstar.com')
            speak('opening Disney+ hotstar')  

        elif 'open sony liv' in query:
            webbrowser.open('sonyliv.com')
            speak('opening sony liv')  
  
        #shopping web---------------------------------------------------------------------------------------------------------------------------

        elif 'open flipkart' in query:
            webbrowser.open('flipkart.com')
            speak('opening flipkart')

        elif 'open amazon' in query:
            webbrowser.open('amazon.in')
            speak('opening amazon')   

        elif 'open meesho' in query:
            webbrowser.open('meesho.com')
            speak('opening meesho') 

        elif 'open nykaa' in query:
            webbrowser.open('nykaa.com')
            speak('opening nykaa') 

        elif 'open purple' in query:
            webbrowser.open('purplle.com')
            speak('opening purple')

        elif 'open myntra' in query:
            webbrowser.open('myntra.com')
            speak('opening myntra') 

        elif 'open ajio' in query:
            webbrowser.open('ajio.com')
            speak('opening ajio') 

        elif 'open snapdeal' in query:
            webbrowser.open('snapdeal.com')
            speak('opening snapdeal')  

        elif 'open Tata cliq' in query:
            webbrowser.open('tatacliq.com')
            speak('opening tata cliq')

        #social platform------------------------------------------------------------------------------------------------------------------------

        elif 'open facebook' in query:
            speak('dear what should i do search for you in this')
            cmd = takeCommand()
            if 'nothing' in cmd:
                speak('ok dear, opening facebook')
                webbrowser.open('facebook.com')
            elif 'search' in cmd:
                speak('sure')
                cmd = cmd.replace('search','')
                webbrowser.open(f'facebook.com/{cmd}')
             
        elif 'open instagram' in query:
            speak('dear what should i do search for you in this')
            cmd = takeCommand()
            if 'nothing' in cmd:
                speak('ok dear, opening instagram')
                webbrowser.open('instagram.com')
            elif 'search' in cmd:
                speak('sure')
                cmd = cmd.replace('search','')
                webbrowser.open(f'instagram.com/{cmd}')
            elif 'messages' in cmd:
                webbrowser.open('instagram.com/direct/inbox')       
            
        elif 'open telegram' in query:
            webbrowser.open('https://web.telegram.org/')
            speak('opening telegram') 

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')
            speak('opening whatsapp')                     

        elif 'open twitter' in query:
            speak('dear what should i do search for you in this')
            cmd = takeCommand()
            if 'nothing' in cmd:
                speak('ok dear, opening twitter')
                webbrowser.open('https://twitter.com/RealBenjizo')
            elif 'search' in cmd:
                speak('sure')
                cmd = cmd.replace('search','')
                webbrowser.open(f'https://twitter.com/{cmd}')
            elif 'messages' in cmd:
                speak('sure')
                webbrowser.open(f'https://twitter.com/message')
                      
        #ms-office-------------------------------------------------------------------------------------------------------------------------------
        # --------------open---------------  

        elif 'open powerpoint' in query:
            speak("opening Microsoft Power Point ")
            power = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(power) 

        elif 'open publisher' in query:
            speak("opening Microsoft Publisher ")
            publisher = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Publisher.lnk"
            os.startfile(publisher)  

        elif 'open access' in query:
            speak('opening microsoft Access')
            acc = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access.lnk"
            os.startfile(acc)    

        elif 'open excel' in query:
            speak("opening Microsoft Excel ")
            excel = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
            os.startfile(excel)  

        elif 'open word' in query:
            speak("opening Microsoft Word")
            word = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(word) 

        elif 'open one drive' in query:
            speak("opening Microsoft One Drive ")
            oned = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneDrive.lnk"
            os.startfile(oned)   
         
        #ms-office----------------------------------------------------------------------------------------------------------
        #--------------close---------------

        elif 'close powerpoint' in query:
            speak('ok dear, closing Microsoft Word')
            os.system("taskkill /f /im POWERPNT.exe") 

        elif 'close publisher' in query:
            speak('ok dear, closing Microsoft Word')
            os.system("taskkill /f /im WINWORD.exe")  

        elif ' close access' in query:
            speak('ok dear, closing Microsoft Word')
            os.system("taskkill /f /im MSACCESS.exe")    

        elif 'close excel' in query:
            speak('ok dear, closing Microsoft Word')
            os.system("taskkill /f /im EXCEL.exe")  

        elif 'close ms word' in query:
            speak('ok dear, closing Microsoft Word')
            os.system("taskkill /f /im WINWORD.exe")
            
        elif 'close one drive' in query:
            speak('ok dear, closing Microsoft Word')
            os.system("taskkill /f /im ONEDRIVE.exe") 

        #broswers-----------------------------------------------------------------------------------------------------------------

        elif 'open brave' in query:
            brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
            try:
                os.startfile(brave_path)
                speak('opening brave')
            except Exception as e:
                speak("Sorry dear i cant find this or you didnt download in your system")     

        elif 'open chrome' in query:
            chrome_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Chrome.lnk"
            try:
                os.startfile(chrome_path)
                speak('opening chrome')
            except Exception as e:
                speak("Sorry dear i cant find this or you didnt download in your system") 

        elif 'open firefox' in query:
            firefox_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk"
            try:
                os.startfile(firefox_path)
                speak('opening firefox')
            except Exception as e:
                speak("Sorry dear i cant find this or you didnt download in your system") 

        elif 'open opera' in query:
            opera_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Opera.lnk"
            try:
                os.startfile(opera_path)
                speak('opening firefox')
            except Exception as e:
                speak("Sorry dear i cant find this or you didnt download in your system")    
                                 
        #others workings----------------------------------------------------------------------------------------------------------------------------------------- 

        elif "write a note" in query:
            speak("What should i write, dear")
            note = takeCommand()
            file = open('text.txt', 'w')
            speak("Dear, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Which one , name please")
            file1 = takeCommand()
            file = open(file1, "r")
            print(file.read())
            speak(file.read(6))
         
        #maths and expert level questioning       

        if "calculate" in query:
            question = query.replace('calculate','')
            client = wolframalpha.Client(os.getenv('app_id'))
            res = client.query(question)
            try:
                answer = next(res.results).text
                speak(f'The answer is {answer}')
                print(answer)
            except StopIteration:
                speak("I'm sorry, I could not find an answer to that question.")


        elif "what is the" in query:  
            try:
                question = query.replace('what is the','')
                client = wolframalpha.Client(os.getenv('app_id'))
                res = client.query(question)
                answer = next(res.results).text
                speak(f'The answer is {str(answer)}')
                print(answer) 
            except:
                question = query.replace('what is the', '')
                client = wolframalpha.Client(os.getenv('app_id'))
                res = client.query(question)
                answer = next(res.results).text
                speak(f'The answer is {str(answer)}')
                print(answer)
        

        elif "difference between" in query:
            query = query.replace('difference between','')
            webbrowser.open(f'difference between {query}')
            speak('here are some results')    

        elif 'sms' in query or 'text' in query:
            account_sid = os.getenv('sms_api_id')
            auth_token = os.getenv('sms_api_auth')
            #print(account_sid, auth_token)
            client = Client(account_sid, auth_token)  
            speak('tell me the number dear whose want to send the message')
            recipient = takeCommand()
            number = f'+91{recipient}'
            system_number = os.getenv('sms_secret_number') 
            #print(system_number)
            speak('tell me what should i write')
            msg = takeCommand()
            message = client.messages.create(to=number , from_=system_number, body=msg)  
            print(message.sid)


        elif 'whatsapp message' in query:
            speak('tell me the number')
            num = takeCommand()
            speak('ok, what should i write')
            msg = takeCommand()
            send_whatsapp_message(num, msg) 
            speak('message has been sent')     