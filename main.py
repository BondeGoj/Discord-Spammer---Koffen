import time
import keyboard
import random
import os
import sys
import ctypes
from getpass import getpass
import stdiomask

a = 0
os.system("cls")
Grey = "\033[1;30;40m"
White = "\033[0;37m"
Yellow = "\033[0;33m"
Blue = "\033[0;34m"
Red = "\033[31m"
Green = "\033[0;32m"
Pink = "\033[0;35m"

FingerMan = """:mechanical_arm: :laughing::middle_finger:
:mechanical_leg::full_moon: :mechanical_leg:
"""
CatMan = """:muscle: :smirk_cat: :call_me:"""

ctypes.windll.kernel32.SetConsoleTitleA(" ")

def countdown():
    counter = 10
    while not(counter==0):
        counter -= 1
        print(White + "Starting in "+Red, counter, White)
        time.sleep(1)
        os.system('cls||clear')
        asciiText()

def asciiText():
    print(White + """     ,--.-.,-.   _,.---._        _,---.      _,---.     ,----.  .-._         
    /==/- |\  \,-.' , -  `.   .-`.' ,  \  .-`.' ,  \ ,-.--` , \/==/ \  .-._  
    |==|_ `/_ /==/_,  ,  - \ /==/_  _.-' /==/_  _.-'|==|-  _.-`|==|, \/ /, / 
    |==| ,   /==|   .=.     /==/-  '..-./==/-  '..-.|==|   `.-.|==|-  \|  |  
    |==|-  .||==|_ : ;=:  - |==|_ ,    /|==|_ ,    /==/_ ,    /|==| ,  | -|  
    |==| _ , \==| , '='     |==|   .--' |==|   .--'|==|    .-' |==| -   _ |  
    /==/  '\  \==\ -    ,_ /|==|-  |    |==|-  |   |==|_  ,`-._|==|  /\ , |  
    \==\ /\=\.''.='. -   .' /==/   \    /==/   \   /==/ ,     //==/, | |- |  
     `--`        `--`--''   `--`---'    `--`---'   `--`-----`` `--`./  `--`                                         
    """)
    print(Blue + "\t\t Discord bondegoj#9688 \n\n")

def Credit():
    print(White+"Made by danikof (Discord: bondegoj#9688) \n")
    print(White + "[", Blue + "1", White + "]", Blue + "Back to menu")
    back = input(">"+White)
    os.system('cls||clear')
    menu()

def selfWriter():
    print(Blue)
    spamCounter = int(input("How many times to spam> "+White))

    countdown()
    a = 0
    while not(a==spamCounter):
        keyboard.write("﷽﷽﷽﷽﷽﷽﷽")
        keyboard.press_and_release('enter')
        a += 1
        os.system('cls||clear')
        asciiText()
        print(a, "out of", spamCounter, White,)

    os.system("pause")
    os.system('cls||clear')
    menu()

def controlSpamText():
    spamTextControled = input("Text to spam> "+White)
    spamCounter = int(input(Blue+"How many times to spam> "+White))

    a = 0
    countdown()

    while not(a==spamCounter):
        keyboard.write(spamTextControled)
        keyboard.press_and_release('enter')
        a += 1
        os.system('cls||clear')
        asciiText()
        print(a, "out of", spamCounter, White,)

    os.system("pause")
    os.system('cls||clear')
    menu()

def discordSpamText():
    spamCounter = int(input(Blue + "How many times to spam> " + White))
    print(White + "[", Blue + "1", White + "]", Blue + "Finger Man")
    print(White + "[", Blue + "2", White + "]", Blue + "Baddie Cat")
    print(White+"More coming soon...")
    print("")
    spamType = int(input("> " + White))

    a = 0
    countdown()
    while not (a == spamCounter):
        if spamType == 1:
            keyboard.write(FingerMan)
        if spamType == 2:
            keyboard.write(CatMan)
        keyboard.press_and_release('enter')
        a += 1
        os.system('cls||clear')
        asciiText()
        print(a, "out of", spamCounter, White,)
        time.sleep(0.10)

    os.system("pause")
    os.system('cls||clear')
    menu()


def menu():
    asciiText()
    print(White+"[", Blue + "1", White + "]", Blue + "Credit")
    print(White+"[", Blue + "2", White + "]", Blue + "Self writer")
    print(White+"[", Blue + "3", White + "]", Blue + "Control spam text")
    print(White+"[", Blue + "4", White + "]", Blue + "Custom spam text (Only for discord)")
    menuchoice = input("> "+White)

    if (str(menuchoice)) == "1":
        os.system('cls||clear')
        asciiText()
        Credit()
    elif (str(menuchoice)) == "2":
        os.system('cls||clear')
        asciiText()
        selfWriter()
    elif (str(menuchoice)) == "3":
        os.system('cls||clear')
        asciiText()
        controlSpamText()
    elif (str(menuchoice)) == "4":
        os.system('cls||clear')
        asciiText()
        discordSpamText()

    while (str(menuchoice) not in ["1", "2", "3", "4"]):
        print("\"" + menuchoice + "\" isnt a valid option, try again.")
        time.sleep(1)
        os.system('cls||clear')
        menu()

menu()
