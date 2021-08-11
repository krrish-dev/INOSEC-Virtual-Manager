
# Copyright 2021 krrish, All rights reserved.
# You are not allowed to use this code to represent yoursself in the front of outsiders as you do from
# from stackoverflow or form github,
# Coperate with us. THANK YOU

# Written by a Indian Developer - username on GitHub: @krrish-dev #

# implementing modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from nltk.corpus import wordnet
import speech_recognition as sr
import wikipedia
import pyttsx3
import feedparser
import webbrowser
import sys
import time


# logo
print('''\n\n
###########################################################   ??    ??   
#        ##  ##### ##       ##      ##       ##       #####  ?  ?  ? ?   
####  ##### # #### ## ##### ## ####### ######## ###########  ?  ?    ?   
####  ##### ## ### ## ##### ## ####### ######## ###########   ??   ????? 
####  ##### ### ## ## ##### ##      ##       ## ##########################
####  ##### #### # ## ##### ####### ## ######## ######  ####  #  #####  ##
####  ##### #####  ## ##### ####### ## ######## ####### #### ## # ### # ##
#        ## ###### ##       ##      ##       ##       ## ## ### ## # ## ##
#########################################################  ####  ##  #  ##
##########################################################################
''')

print('\n\nVIRTUAL MANAGER')

print('\nwait while enstalizing|...')

#chat program 
# chatterbot module is used for creating a chat bot but here I had used it to make AI based talking assistant to support the program
bot = ChatBot('Bot')
trainer = ListTrainer(bot)
# training a bot by implementing some random chats you can also another one according to your need
trainer.train([
'hi',
'hello',
'hey',
'hay',
'good evening',
'good evening',
'how are you',
'I am fine',
'thats good to hear',
'who are you',
'I am a virtual manager on your system',
'who created you',
'I was created by an Indian developer',
'who is your favourite person',
'the one who had created me',
'I am depressed',
'ohh can I play a song for you',
'yes',
'give me a applicable commands for playing a song',
'thanks for playing a song',
'or what are you doning',
'just felling you well',
'hey you are very bad',
'sorry if I commited any mistake',
'I know that I am not like alexa and siri but I am not worse as you think',
'fuck off',
'dont abuse me idiot',
'I will not talk to you, if you abuse me',
'good night',
'good  night'
])


def chat_talk(req):
    if req == 'bye':
        speak("bye bye, if you want me to exit then say exit")
    else:
        response = bot.get_response(req)
        print(response)
        speak(response)


#voice creating engine
def speak(audio):
    atul_s = pyttsx3.init()
    atul_s.setProperty('voice', 'english_rp+f4') # voice id[currently female voice], change 'f4' to 'f6' to make a male voice
    atul_s.setProperty("rate", 140)
    atul_s.say(audio)
    atul_s.runAndWait()

#microphone accessing engine
def atul_speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("Speak now... ")
        audio= r.listen(source, timeout=0)
        try:
            print('Recognising...')
            text = r.recognize_google(audio) # google is used a recognision tool
            print('you: ', text)
            return text
        except:
            print('could not recognise your voice!!')
            speak("say that again or give command silent")
            return atul_speak()

#basic commands or user input and working of the whole program
def commands():
    while(True):
        # all the commands are programmed over here
        atul_lis = atul_speak().lower()
        if 'good morining' in atul_lis:
            text = "Good Morning"
            speak(text)
        elif 'time' in atul_lis:
            text = time.strftime(" time is %H hours %M minutes %p")
            speak(text)
        elif 'open browser' in atul_lis:
            text = "opening brave as an incognito mode"
            speak(text)
            webbrowser.open()
        elif 'reddit' in atul_lis:
            text = "opening reddit"
            speak(text)
            webbrowser.open("https://www.reddit.com/")
        elif 'youtube' in atul_lis:
            text = "opening youtube"
            speak(text)
            webbrowser.open("https://www.youtube.com")
        elif 'google account' in atul_lis:
            text = "opening your google account"
            speak(text)
            webbrowser.open("https://myaccount.google.com/")
        elif 'gmail account' in atul_lis:
            text = "opening your gmail account"
            speak(text)
            webbrowser.open("https://mail.google.com/mail/")
        elif 'search for wikipedia' in atul_lis:
            speak('opening search bar of wikipedia')
            s = Search_()
            s.atul_ser_main()
        elif 'open twitter' in atul_lis:
            text = "opening your twitter account"
            speak(text)
            webbrowser.open("https://www.twitter.com/")
        elif 'github' in atul_lis:
            text = "opening github"
            speak(text)
            webbrowser.open("https://www.github.com")
        elif 'open facebook' in atul_lis:
            text = "opening facebook"
            speak(text)
            webbrowser.open("https://facebook.com")
        elif 'search on internet' in atul_lis:
            text = "searching it on web"
            speak(text)
            speak("whats your query")
            g_serch()
        elif 'play a song' in atul_lis:
            text = "name a song"
            speak(text)
            s_serch()
        elif 'meaning' in atul_lis:
            speak("your word query")
            mean(atul_speak())
        elif 'silent' in atul_lis:
            # if you are doing some another work it will help you to shut up the microphone recognition, helps you grom getting disturbed, just press enter continue
            text = "you put me on hold, just press enter to continue"
            speak(text)
            print('this required physical interference')
            comman = input('press enter to continue ||||')
            if comman == '':
                pass
            else:
                pass
        elif 'exit' in atul_lis:
            speak("exiting the program")
            time.sleep(1)
            exit()
        elif 'amazon shop' in atul_lis:
            text = "opening a amazon shop"
            speak(text)
            webbrowser.open("https://www.amazon.com/")
        elif 'amazon product' in atul_lis:
            speak("name of your product")
            amazon(atul_speak())
        elif 'news' in atul_lis:
            ne()
        else:
            chat_talk(atul_speak())
            continue


#algo of show news content
def ne():
    text = "todays news"
    speak(text)
    nf = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
    for i in range(1, 10):
        new_f = nf.entries[i]
        news = new_f.summary
        print(news, '\n')
        speak(news)

#algo for searching on web [google.com]
def g_link(query):
    content = str(query).split(" ")
    print(content)
    def que():
        squares = []
        for i in range(0, len(content)):
            z = content[0]
            a = "%20" + content[i]
            squ = squares.append(a)
            listToStr = ''.join([str(elem) for elem in squares])
        return listToStr
    j = str(que())
    return j


def g_serch():
    try:
        g = str(g_link(atul_speak()))
        print(g)
        webbrowser.open("https://www.google.com/search?q=" + g)
    except:
        speak("cannot able to perform system operation")

#algo for palying a song - "soundcloud.com"
def s_link(query):
    content = str(query).split(" ")
    print(content)
    def sque():
        squares = []
        for i in range(0, len(content)):
            z = content[0]
            a = "%20" + content[i]
            squ = squares.append(a)
            listToStr = ''.join([str(elem) for elem in squares])
        return listToStr
    j = str(sque())
    return j


def s_serch():
    try:
        g = str(s_link(atul_speak()))
        print(g)
        webbrowser.open("https://soundcloud.com/search?q=" + g)
    except:
        speak("cannot able to perform system operation")


#amazon algo- "amazon.com"
def amazon(product):
    try:
        lin = "https://www.amazon.com/s?k=" + product
        webbrowser.open(lin)
    except:
        speak("could not perform a operation")

# telling meanings
# it use nltk library to find the meaning of world
def mean(word):
    try:
        syns = wordnet.synsets(word)
        a = syns[0].definition()
        print('meaning ' + a)
        speak("meaning of ")
        speak(word)
        speak(a)
        b = syns[0].examples()
        speak("for example ")
        speak(b)
    except Exception as e:
        print(e)
        speak("cannot find the world or library is not implemented properly")


#class for wekipedia search using wikipedia library
class Search_():
    def __init__(self):
        print('start searching... /')
        
    def wiki_(self):
        while True:
            text_start = 'whats your queery sir...'
            speak(text_start)
            data5 = atul_speak().lower()
            result = wikipedia.summary(data5, sentences=3)
            text1 = '\n', '[', result, ']', '\n'
            print(text1)
            speak(text1)

            print('continue your search by pressing enter, but if you want to exit press "/"\n')
            
            speak("you want to continue you search in wikipedia or exit the wikipedia")
            forward_ = atul_speak().lower()
            if 'exit' in forward_:
                print('exiting')
                speak("exiting")
                time.sleep(1)
                break
            elif 'continue' in forward_:
                speak("okk continue it")
                continue
            else:
                com = '\ncommand not identified'
                speak(com)
                print(forward_)

    def atul_ser_main(self):
        try:
            s = Search_()
            s.wiki_()
        except Exception as e:
            print(e)
            print('if it shows error \n this is because of wrong search type or network issue')
            print('continue your search by pressing enter, but if you want to exit press "/"\n')
            
            speak("you want to continue you search in wikipedia or exit the wikipedia")
            
            while True:
                forward_ = atul_speak().lower()
                if 'exit' in forward_:
                    print('exiting')
                    speak("exiting")
                    time.sleep(1)
                    break
                elif 'continue' in forward_:
                    speak("okk continue it")
                    atul_ser_main()
                else:
                    com = '\ncommand not identified'
                    speak(com)
                    print(forward_)

#work area of whole program
def main_system():
    print('''
    CopyRight 2021 krrish, All rights reserved.
    support this python written program on GitHub: [@krrish-dev]
    Make sure you are connected to internet otherwise program will not recognise you voice as it uses google to do that
    \nI hope you will enjoy
    ''')

    speak('hey, I am activated now')
    commands()


main_system()
