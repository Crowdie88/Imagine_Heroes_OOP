import items
import sys
# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep
# sounds
import winsound
# color und styles
from colorama import init, Fore, Back, Style

init(wrap=False)
init(autoreset=True)

def clear():
        _ = system('cls')

class NPC:
    def __init__(self, name):
        self.Name = name

class Ben(NPC):
    def __init__(self):
        NPC.__init__(self, "Ben")
    def Quest1(self, item, q1):
        print("")
        text1 = ("It's really nice that you are feeling better again.\nYou can give me a hand here, you look like you could fight.\nHere in the area about 3 km north and 2 km west from here, there is a small camp with goblins.\nThese make the area here quite unsafe.\nCan you please take care of that?\nTake this Sword and healing potions and show me how well you can handle it. Then come back to me...")
        for i in text1:
            sys.stdout.write(Fore.LIGHTYELLOW_EX + i)
            sleep(0.04)
        print("")
        print("")
        print(Fore.GREEN + "Continue...", end="")
        input()
        winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        print("")
        item.push(items.Basic_Sword_1Hand)
        item.push(items.Basic_Potion)
        item.push(items.Basic_Potion)
        item.push(items.Basic_Potion)
        text1 = ("Search the goblin camp. It should be located on the map at coordinates Y: -247, X: 498.\nThen return to Ben.")
        q1.append(text1)
        print(Fore.YELLOW + "Quest accepted.")
        print("")
        print("To equip yourself, enter 'inv' to access your inventory.")
        print("For more options, type 'help'")
        
        