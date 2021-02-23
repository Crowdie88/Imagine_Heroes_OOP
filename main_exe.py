# pydub is an alternativ for linux
#from pydub import AudioSegment
#from pydub.playback import play

# skills
import skills
# char information
from char import Char
# math
import math
# enemys
import enemys
# fight
from fight import Fight
# random
import random
# Clear
from clear import C
# Items
import items
# NPC´s
import npc
# Player
from player import Player
# maps
from maps import Borsigwalde, Celtic_Continent
# save and load
import shelve
from pathlib import Path
# music
import audioplayer  
# sounds
import winsound
# help
from help import Help
# text
import text
# color und styles and sys
import sys
from colorama import init, Fore, Back, Style
# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep
# fullscreen
### Attention only for Windows !!!
import ctypes
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_MAXIMIZE = 3
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE) 
init(wrap=False)
init(autoreset=True)


class Game:
    def __init__(self):
        # Input an existing wav filename
        #thunder = input("sounds\\thunder.wav")
        # load the file into pydub
        #sound_thunder = AudioSegment.from_wav("sounds/thunder.wav")
        # play the file
        #play(sound_thunder)
        # loads music and define music class a,b
        
        self.song1 = ("sounds/hintergrundmusik1.mp3")
        self.song2 = ("sounds/hintergrundmusik2.mp3")
        self.song3 = ("sounds/Background_Music_Castemia.mp3")
        self.song4 = ("sounds/Background_Music_Ragnarök_War.mp3")
        self.song5 = ("sounds/regen_gewitter.mp3")
        #audioplayer.AudioPlayer._do_setvolume(10, self.song5)
        self.a = audioplayer.AudioPlayer(self.song1)
        self.b = audioplayer.AudioPlayer(self.song2)
        self.c = audioplayer.AudioPlayer(self.song3)
        self.d = audioplayer.AudioPlayer(self.song4)
        self.e = audioplayer.AudioPlayer(self.song5)
        
        #-----------------------------------------------------
        # starts playing background music on the startpage
        self.d.play(0)
        self.d._do_setvolume(40)
        #self.c.play(0)
        #self.c._do_setvolume(90)
        #-----------------------------------------------------
        # starts the startscreen
        text_imagine = "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######"

        text_heroes = "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######"

        for i in text_imagine:
            sys.stdout.write(Fore.YELLOW + i)
            sleep(0.01)
        print("")
        print("")
        print("")
        for i in text_heroes:
            sys.stdout.write(Style.BRIGHT + Fore.GREEN + i)
            
            sleep(0.01)
        print("")
        print("")
        print(Style.DIM+"This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
        print("")
        while True:
            print("")
            datei = Path("saved_game/game_saved.dir")
            startgame = input("Would you like to start the game? y/n: ")
            if startgame == "y":
                if datei.is_file():
                    while True:
                        q_load = input("You have a saved game, do you want to load it? y/n: ")
                        if q_load == "y":
                            winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                            #play(sound_thunder)
                            self.load()
                            print("")
                            print(Fore.YELLOW + "Game loaded...")
                            print("")
                            return
                        elif q_load == "n":
                            winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                            #play(sound_thunder)
                            print("")
                            text.introduction()
                            break
                        else:
                            print("")
                            print("Wrong input, try again...")
                            print("")
                else:
                    winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                    #play(sound_thunder)
                    print("")
                    # introduction--------------------------------------------------------------------------------------------------------
                    text.introduction()
                    break
                break
            elif startgame == "n":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print("")
                print("The windows is now closing...")
                sleep(3)
                exit()
            else:
                print("")
                print("Wrong input, try again...")
        self.d._do_setvolume(20)
        self.e.play(0)
        self.e._do_setvolume(35)
        text1 = "Oh... hey, so you finally woke up.\nThat's great, I thought you were dying.\nYou're very lucky that I found you in the bay where I go fishing.\nMy name is Ben, by the way."
        for i in text1:
            sys.stdout.write(Fore.LIGHTYELLOW_EX + i)
            sleep(0.04)
        print("")
        #-------------------------------------------- Name -------------------
        while True:
            var1 = True
            print("")
            print(Fore.LIGHTYELLOW_EX + "What is your name, can you remember? ", end='')
            name = input()
            print("")
            for i in name:
                if i.isdigit() or i.isnumeric() or i == "!" or i == "§" or i == "$" or i == "%" or i == "&" or i == "/" or i == "(" or i == ")" or i == "=" or i == "?" or i == "+" or i == "*" or i == "~" or i == "#" or i == ":" or i == "." or i == ";" or i == "," or i == "<" or i == ">" or i == "|" or i == "^^" or i == "^" or i == "°" or i == "{" or i == "[" or i == "]" or i == "}":
                    print("")
                    print("A name should only consist of letters")
                    print("Try again...")
                    print("")
                    var1 = False
                    break
            if name == "":
                print("")
                print("A name should only consist of letters")
                print("Try again...")
                print("")
                var1 = False
                pass
            elif var1 == True:
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print("")
                print(Fore.LIGHTYELLOW_EX + "Allright, your name is", name)
                C().lear()
                break
        print("")        
        text2 = "Ehm... sorry to ask you this, but you were talking really weird stuff when you were sleeping."
        for i in text2:
            sys.stdout.write(Fore.LIGHTYELLOW_EX + i)
            sleep(0.04)
        #--------------------------------------------- Gender ------------------
        print("")
        while True:
            print("")
            print(Fore.LIGHTYELLOW_EX + "Do you know your gender? Are you female 'w' or male 'm': ", end="")
            gender = input()
            print("")
            if gender == "w":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print(Fore.LIGHTYELLOW_EX + "Thats right, you are female.")
                C().lear()
                break
            elif gender == "m":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print(Fore.LIGHTYELLOW_EX + "Thats right, you are male.")
                C().lear()
                break
            else:
                print("")
                print("Wrong input, try again...")
                print("")
        #--------------------------------------------- Race -----------------
        print("")        
        text2 = "I have one last question for you. Just to make sure you're really okay."
        for i in text2:
            sys.stdout.write(Fore.LIGHTYELLOW_EX + i)
            sleep(0.04)
        print("")
        while True:
            text3 = "Are you aware of which ancestors you descend from?"
            for i in text3:
                sys.stdout.write(Fore.LIGHTYELLOW_EX + i)
                sleep(0.04)
            print("")
            print("")
            print(Fore.BLUE+"(1) Human:")
            print("     - Humans are very tough creatures.")
            print("       In the course of time, they have been able to adapt to any situation and thus have survived.")
            print("       With their adaptability they have + 5% chance of blocking with the right equipment")
            print("")
            print(Fore.YELLOW+"(2) Nefler:")
            print("     - Neflers are nimble cunning creatures.")
            print("       Their advantage is that their skill more than makes up for their lack of strength.")
            print("       Their agile nature, gives them an advantage and therefore have + 3% chance of 2nd attack.")
            print("")
            print(Fore.GREEN+"(3) Kro'L:")
            print("     - Kro'L are parasites.")
            print("       They nest in other living beings, otherwise they have no chance of survival. In this way,")
            print("       they take control of their host and thus develop their enormous potential.  + 10% more life from all sources")
            print("")
            print(Fore.LIGHTYELLOW_EX + "Enter 1, 2 or 3: ", end="")
            race = input()
            if race == "1":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print("")
                print(Fore.LIGHTYELLOW_EX + "That's right too. Great!")
                race = "Human"
                C().lear()
                break
            elif race == "2":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print("")
                print(Fore.LIGHTYELLOW_EX + "That's right too. Great!")
                print("")
                race = "Nefler"
                C().lear()
                break
            elif race == "3":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                #play(sound_thunder)
                print("")
                print(Fore.LIGHTYELLOW_EX + "That's right too. Great!")
                print("")
                race = "Kro'L"
                C().lear()
                break
            else:
                print("")
                print("Wrong input, try again...")
                print("")
        
        # Game Variables ##########################################################################################
        # Equipment Bonus:
#--------------------------------------------------
        # 2x 1-Hand +3% 2nd Attack
        self.switch_bonus_on_2_1hand = False
        self.switch_bonus_off_2_1hand = False
        self.switch_2_1hand = False
        # 1x 2-Hand +7% total damage
        self.switch_bonus_on_1_2hand = False
        self.switch_bonus_off_1_2hand = False
        self.switch_1_2hand = False
        # Shield +5% bonus armor
        self.switch_bonus_on_shield = False
        self.switch_bonus_off_shield = False
        self.switch_shield = False
        # Leather + 5% bonus 2nd attack
        self.switch_bonus_on_Leather = False
        self.switch_bonus_off_Leather = False
        self.switch_Leather = False
        # Chain + 8% bonus total damage
        self.switch_bonus_on_Chain = False
        self.switch_bonus_off_Chain = False
        self.switch_Chain = False
        # Plate +3% armor and 2% blockchance
        self.switch_bonus_on_Plate = False
        self.switch_bonus_off_Plate = False
        self.switch_Plate = False
        # Ben Quest Variables -----------------------------
        self.ben_quest_1 = []
        # Ben Reward Variables -----------------------------
        self.ben_reward_1 = []
        

        # init Player --------------------------------------------------------------------------------
        self.Player1 = Player(name, gender, race)
        #-----------------------------------------------------
        ##############################################################################################################################################
        
        ####################################################---- Control Loop ----#######################################################################
    def main(self):
        while True:
            # Equippment Bonus
            # 2x 1-Hand Weapon Bonus 3% on/off Attack2
            if len(self.Player1.getHands()[0]) == 1 and len(self.Player1.getHands()[1]) == 1 and len(self.Player1.getHands()[2]) == 0 and self.Player1.getHands()[1][0].getCategory() == "Weapon":
                self.switch_bonus_on_2_1hand = True
            else:
                self.switch_2_1hand = True
            if self.switch_bonus_off_2_1hand == True and self.switch_2_1hand == True:
                self.Player1.setAttack2(self.Player1.Attack2 - 3)
                print(Fore.YELLOW + "You lose your 3% bonus on 2nd attack")
                self.switch_bonus_off_2_1hand = False
                self.switch_bonus_on_2_1hand = False
            if self.switch_bonus_on_2_1hand == True and self.switch_bonus_off_2_1hand == False and self.Player1.getThe_Berserker() == True:
                self.Player1.setAttack2(self.Player1.Attack2 + 3)
                print(Fore.YELLOW + "By carrying 2x 1-handed weapon, you get a 3% bonus on chance for 2nd attack")
                self.switch_bonus_off_2_1hand = True
                self.switch_2_1hand = False
            # -------------------------------------------------------------------------------------------------------------
            # 1x 2-Hand Weapon Bonus 7% on/off total damage
            if len(self.Player1.getHands()[2]) == 1 and self.Player1.getHands()[2][0].getCategory() == "Weapon":
                self.switch_bonus_on_1_2hand = True
            else:
                self.switch_1_2hand = True
            if self.switch_bonus_off_1_2hand == True and self.switch_1_2hand == True:
                print(Fore.LIGHTRED_EX + "You lose your 7% bonus on total damage")
                self.switch_bonus_off_1_2hand = False
                self.switch_bonus_on_1_2hand = False
            if self.switch_bonus_on_1_2hand == True and self.switch_bonus_off_1_2hand == False and self.Player1.getThe_Warrior() == True:
                print(Fore.LIGHTRED_EX + "Carrying a 2-handed weapon gives you a 7% bonus on your total damage")
                self.switch_bonus_off_1_2hand = True
                self.switch_1_2hand = False
            #------------------------------------------------------------------------------------------------------------------
            # Shild Bonus reduction decrased to 8 instead of 10
            if len(self.Player1.getHands()[1]) == 1 and self.Player1.getHands()[1][0].getCategory() == "Armor":
                self.switch_bonus_on_shield = True
            else:
                self.switch_shield = True
            if self.switch_bonus_off_shield == True and self.switch_shield == True and self.Player1.getThe_Defender() == True:
                print(Fore.LIGHTBLUE_EX + "You lose your bonus. The required armor value has been increased again.")
                self.switch_bonus_off_shield = False
                self.switch_bonus_on_shield = False
            if self.switch_bonus_on_shield == True and self.switch_bonus_off_shield == False and self.Player1.getThe_Defender() == True:
                if self.Player1.getThe_Defender() == True:
                    print(Fore.LIGHTBLUE_EX + "Reduces the armor value needed to absorb damage by 2.")
                self.switch_bonus_off_shield = True
                self.switch_shield = False
            #------------------------------------------------------------------------------------------------------------------
            # Leather 5% bonus 2nd attack
            if len(self.Player1.getHead()) == 1 and len(self.Player1.getBody()) == 1 and len(self.Player1.getLegs()) == 1 and len(self.Player1.getFeet()) == 1 and self.Player1.getHead()[0].getMaterial() == "Leather" and self.Player1.getBody()[0].getMaterial() == "Leather" and self.Player1.getLegs()[0].getMaterial() == "Leather" and self.Player1.getFeet()[0].getMaterial() == "Leather":
                self.switch_bonus_on_Leather = True
            else:
                self.switch_Leather = True
            if self.switch_bonus_off_Leather == True and self.switch_Leather == True:
                self.Player1.setAttack2(self.Player1.Attack2 - 5)
                print(Fore.LIGHTMAGENTA_EX + "You lose your 5% bonus on 2nd attack")
                self.switch_bonus_off_Leather = False
                self.switch_bonus_on_Leather = False
            if self.switch_bonus_on_Leather == True and self.switch_bonus_off_Leather == False:
                self.Player1.setAttack2(self.Player1.Attack2 - 5)
                print(Fore.LIGHTMAGENTA_EX + "Because your armor is made entirely of leather, you get a 5% bonus on 2nd attack")
                self.switch_bonus_off_Leather = True
                self.switch_Leather = False
            #--------------------------------------------------------------------------------------------------------------------
            # Chain 8% bonus total damage
            if len(self.Player1.getHead()) == 1 and len(self.Player1.getBody()) == 1 and len(self.Player1.getLegs()) == 1 and len(self.Player1.getFeet()) == 1 and self.Player1.getHead()[0].getMaterial() == "Chain" and self.Player1.getBody()[0].getMaterial() == "Chain" and self.Player1.getLegs()[0].getMaterial() == "Chain" and self.Player1.getFeet()[0].getMaterial() == "Chain":
                self.switch_bonus_on_Chain = True
            else:
                self.switch_Chain = True
            if self.switch_bonus_off_Chain == True and self.switch_Chain == True:
                print(Fore.LIGHTMAGENTA_EX + "You lose your 8% bonus on total damage")
                self.switch_bonus_off_Chain = False
                self.switch_bonus_on_Chain = False
            if self.switch_bonus_on_Chain == True and self.switch_bonus_off_Chain == False:
                print(Fore.LIGHTMAGENTA_EX + "Because your armor is made entirely of chain, you get a 8% bonus on total damage")
                self.switch_bonus_off_Chain = True
                self.switch_Chain = False
            #---------------------------------------------------------------------------------------------------------------------
            # Plate increase 1 dmg reduction + 2% blockchance
            if len(self.Player1.getHead()) == 1 and len(self.Player1.getBody()) == 1 and len(self.Player1.getLegs()) == 1 and len(self.Player1.getFeet()) == 1 and self.Player1.getHead()[0].getMaterial() == "Plate" and self.Player1.getBody()[0].getMaterial() == "Plate" and self.Player1.getLegs()[0].getMaterial() == "Plate" and self.Player1.getFeet()[0].getMaterial() == "Plate":
                self.switch_bonus_on_Plate = True
            else:
                self.switch_Plate = True
            if self.switch_bonus_off_Plate == True and self.switch_Plate == True:
                self.Player1.setBlockchance(self.Player1.Blockchance - 2)
                print(Fore.LIGHTMAGENTA_EX + "You lose your bonus. The required armor value has been increased again. and 2% increased blocking chance")
                self.switch_bonus_off_Plate = False
                self.switch_bonus_on_Plate = False
            if self.switch_bonus_on_Plate == True and self.switch_bonus_off_Plate == False:
                self.Player1.setBlockchance(self.Player1.Blockchance + 2)
                print(Fore.LIGHTMAGENTA_EX + "Because your Armor is made entirely of Plate, reduces the armor value needed to absorb damage by 1 and a 2% increased blocking chance")
                self.switch_bonus_off_Plate = True
                self.switch_Plate = False
            #-- Armor bonus controll ----------- both bonus -----------------------------------------------------
            if self.switch_bonus_on_Plate == True and self.switch_bonus_on_shield and self.Player1.getThe_Defender() == True:
                self.Player1.setReductionBonus(7)
            #--------------------only armor
            elif self.switch_bonus_on_Plate == True and self.switch_bonus_off_shield == False:
                self.Player1.setReductionBonus(9)
            #--------------------only shield
            elif self.switch_bonus_on_Plate == False and self.switch_bonus_on_shield and self.Player1.getThe_Defender() == True:
                self.Player1.setReductionBonus(8)
            #--------------------no bonus
            elif self.switch_bonus_on_Plate == False and self.switch_bonus_off_shield == False:
                self.Player1.setReductionBonus(10)
            #-- Dmg bonus controll ------------------- both bonus ------------------------------------------------------
            if self.switch_bonus_on_1_2hand and self.switch_bonus_on_Chain and self.Player1.getThe_Warrior() == True:
                self.Player1.setDmg(0)
                if self.Player1.getDmg() < 585:
                    self.Player1.setDmg(math.floor(self.Player1.Dmg+((self.Player1.getHands()[2][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 15)))
                else:
                    self.Player1.setDmg(math.ceil(self.Player1.Dmg+((self.Player1.getHands()[2][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 15)))
            #--------------------only weapon
            elif self.switch_bonus_on_1_2hand and self.switch_bonus_on_Chain == False and self.Player1.getThe_Warrior() == True:
                self.Player1.setDmg(0)
                if self.Player1.getDmg() < 585:
                    self.Player1.setDmg(math.floor(self.Player1.Dmg+((self.Player1.getHands()[2][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 7)))
                else:
                    self.Player1.setDmg(math.ceil(self.Player1.Dmg+((self.Player1.getHands()[2][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 7)))
            #--------------------only armor
            elif self.switch_bonus_on_1_2hand == False and self.switch_bonus_on_Chain:
                self.Player1.setDmg(0)
                if self.Player1.getDmg() < 585:
                    if len(self.Player1.getHands()[0]) == 1 and len(self.Player1.getHands()[1]) == 0:
                        self.Player1.setDmg(math.floor(self.Player1.Dmg+((self.Player1.getHands()[0][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 8)))
                    elif len(self.Player1.getHands()[0]) == 0 and len(self.Player1.getHands()[1]) == 1 and self.Player1.getHands()[1][0].getCategory() == "Weapon":
                        self.Player1.setDmg(math.floor(self.Player1.Dmg+((self.Player1.getHands()[1][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 8)))
                    elif len(self.Player1.getHands()[1]) == 1 and len(self.Player1.getHands()[1]) == 1 and self.Player1.getHands()[1][0].getCategory() == "Weapon":
                        self.Player1.setDmg(math.floor(self.Player1.Dmg+((self.Player1.getHands()[1][0].getMaxDmg() + self.Player1.getHands()[0][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 8)))
                else:
                    if len(self.Player1.getHands()[0]) == 1 and len(self.Player1.getHands()[1]) == 0:
                        self.Player1.setDmg(math.ceil(self.Player1.Dmg+((self.Player1.getHands()[0][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 8)))
                    elif len(self.Player1.getHands()[0]) == 0 and len(self.Player1.getHands()[1]) == 1 and self.Player1.getHands()[1][0].getCategory() == "Weapon":
                        self.Player1.setDmg(math.ceil(self.Player1.Dmg+((self.Player1.getHands()[1][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 8)))
                    elif len(self.Player1.getHands()[1]) == 1 and len(self.Player1.getHands()[1]) == 1 and self.Player1.getHands()[1][0].getCategory() == "Weapon":
                        self.Player1.setDmg(math.ceil(self.Player1.Dmg+((self.Player1.getHands()[1][0].getMaxDmg() + self.Player1.getHands()[0][0].getMaxDmg() + self.Player1.getStrength()) / 100 * 8)))
            #--------------------no bonus
            elif self.switch_bonus_on_1_2hand == False and self.switch_bonus_on_Chain == False:
                self.Player1.setDmg(0)
                
            # Game controls for the player---------------------------------------------------------------------------------------------------
            print("")
            options = input("Options: ")
            print("")
            # move in western direction ---------------------------------------------------------------------------------------------
            if options == "d":
                if self.Player1.x < Celtic_Continent.width:
                    self.Player1.move("d")
                    print("")
                    print("You run 1 km in eastern direction")
                    print("")
                else:
                    print("")
                    print("The sea blocks your way")
                    print("")
                break
            # move in eastern direction ---------------------------------------------------------------------------------------------
            elif options == "a":
                if self.Player1.x > -(Celtic_Continent.width):
                    self.Player1.move("a")
                    print("")
                    print("You run 1 km in western direction")
                    print("")
                else:
                    print("")
                    print("The sea blocks your way")
                    print("")
                break
            # move in northern direction ---------------------------------------------------------------------------------------------
            elif options == "w":
                if self.Player1.y < Celtic_Continent.height:
                    self.Player1.move("w")
                    print("")
                    print("You run 1 km in northern direction")
                    print("")
                else:
                    print("")
                    print("Snow covered mountains block your way")
                    print("")
                break
            # move in southern direction ---------------------------------------------------------------------------------------------
            elif options == "s":
                if self.Player1.y > -(Celtic_Continent.height):
                    self.Player1.move("s")
                    print("")
                    print("You run 1 km in southern direction")
                    print("")
                else:
                    print("")
                    print("The sea blocks your way")
                    print("")
                break
            elif options == "help":
                Help().getHelp()
            # Map---------------------------------------------------------------------------------------------------------------------
            elif options == "map":
                print("Location:", Celtic_Continent.getName(), "  Coordinates: Y:", self.Player1.y,", X:", self.Player1.x)
                
            # Quit --------------------------------------------------------------------------------------------------------------------
            elif options == "quit":
                winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                print("")
                print("The windows is now closing...")
                sleep(3)
                exit()
            # Inventory ----------------------------------------------------------------------------------------------------------------
            elif options == "inv":
                self.Player1.getInventory()
            # Skills -------------------------------------------------------------------------------------------------------------------
            elif options == "skills":
                skills.Skills().getSkills(self.Player1)
            elif options == "dmg":
                print(self.Player1.getDmg())
            # Quest_log -----------------------------------------------------------------------------------------------------------------
            elif options == "q":
                self.Player1.getQlog()
            # save ----------------------------------------------------------------------------------------------------------------------
            elif options == "save":
                self.save()
                print("")
                print(Fore.YELLOW + "Game saved...")
                print("")
            # load ------------------------------------------------------------------------------------------------------------------------
            elif options == "load":
                self.load()
                print("")
                print(Fore.YELLOW + "Game loaded...")
                print("")
            elif options == "name":
                print(self.Player1.getName())
            elif options == "dmg":
                print(self.Player1.getDmg())
            elif options == "str":
                self.Player1.setStrength(self.Player1.getStrength() + 2)
            elif options == "block":
                print(self.Player1.getBlockchance())
            elif options == "xp":
                print(len(self.Player1.Xp))
            elif options == "attack":
                print(self.Player1.getAttack2())
            elif options == "armor":
                print(self.Player1.getArmor())
            elif options == "char":
                Char(self.Player1).getchar_info(self.Player1.Dmg)

            elif options == "rest":
                print(Fore.YELLOW + "You rest by a homemade campfire.")
                print(Fore.YELLOW + "You regenerate 10% of your maximum life every 1.5 seconds in the course of 7.5 seconds")
                print("")
                for i in range(5):
                    sleep(1.5)
                    if self.Player1.getRace() == "Kro'L":
                        if self.Player1.getHealth() < (math.floor(self.Player1.getMaxHealth() * 0.9)):
                            self.Player1.setHealth(self.Player1.getHealth() + math.ceil(self.Player1.getMaxHealth() * 0.1))
                            print(Fore.GREEN + "You regenerate", math.ceil(self.Player1.getMaxHealth() * 0.1), Fore.GREEN + "life points")
                            print("")
                        elif self.Player1.getHealth() >= (math.floor(self.Player1.getMaxHealth() * 0.9)):
                            self.Player1.setHealth(self.Player1.getMaxHealth())
                            print(Fore.GREEN + "Your life points have been completely regenerated")
                            print("")
                            break
                    else:
                        if self.Player1.getHealth() < (math.floor(self.Player1.getMaxHealth() * 0.9)):
                            self.Player1.setHealth(self.Player1.getHealth() + math.floor(self.Player1.getMaxHealth() * 0.1))
                            print(Fore.GREEN + "You regenerate", math.floor(self.Player1.getMaxHealth() * 0.1), Fore.GREEN + "life points")
                            print("")
                        elif self.Player1.getHealth() >= (math.floor(self.Player1.getMaxHealth() * 0.9)):
                            self.Player1.setHealth(self.Player1.getMaxHealth())
                            print(Fore.GREEN + "Your life points have been completely regenerated")
                            print("")
                            break
                print(Fore.GREEN + "Your currently health:", self.Player1.getHealth())
            else:
                print("")
                print("Wrong input, try again...")
                print("")
            
    #--------------------------------------------------------------------------------------------------------------------------------
    def area_enemy_goblins(self):
        if self.Player1.y > -250 and self.Player1.x < 500:
            while True:
                dice = random.randint(1,100)
                if dice <= 25:
                    list_goblins = [enemys.Goblin(), enemys.Goblin()]
                    Fight(self.Player1, list_goblins).getfight()
                    break
                else:
                    break
    #----------------------------------------------------------------------------------------------------------- Quests Ben ---------------------
    def ben_q1(self):
        while len(self.ben_quest_1) == 0:
            npc.Ben().Quest1(self.Player1, self.Player1.quest_log)
            self.ben_quest_1.append("q1")
            self.e._dostop()
            self.d._do_setvolume(30)
            break
    #------------------------------------------------------------------------------------------------------------ Rewards Ben ----------------------
    def ben_reward1(self):
        while self.ben_reward_1 == 1:
            break
    # saves the Game #####################################################################################################################
    def save(self):
        db = shelve.open('saved_game\\game_saved')

        db['Object1'] = self.Player1
        db['Object2'] = self.ben_quest_1
        db['Object3'] = self.switch_bonus_on_2_1hand
        db['Object4'] = self.switch_bonus_off_2_1hand
        db['Object5'] = self.switch_2_1hand
        db['Object6'] = self.switch_bonus_on_1_2hand
        db['Object7'] = self.switch_bonus_off_1_2hand
        db['Object8'] = self.switch_1_2hand
        db['Object9'] = self.switch_bonus_on_shield
        db['Object10'] = self.switch_bonus_off_shield
        db['Object11'] = self.switch_shield
        db['Object12'] = self.switch_bonus_on_Leather
        db['Object13'] = self.switch_bonus_off_Leather
        db['Object14'] = self.switch_Leather
        db['Object15'] = self.switch_bonus_on_Chain
        db['Object16'] = self.switch_bonus_off_Chain
        db['Object17'] = self.switch_Chain
        db['Object18'] = self.switch_bonus_on_Plate
        db['Object19'] = self.switch_bonus_off_Plate
        db['Object20'] = self.switch_Plate
        db.close()
    # loads the Game #####################################################################################################################
    def load(self):
        db=shelve.open('saved_game\\game_saved')

        self.Player1=(db['Object1'])
        self.ben_quest_1=(db['Object2'])
        self.switch_bonus_on_2_1hand=(db['Object3'])
        self.switch_bonus_off_2_1hand=(db['Object4'])
        self.switch_2_1hand=(db['Object5'])
        self.switch_bonus_on_1_2hand=(db['Object6'])
        self.switch_bonus_off_1_2hand=(db['Object7'])
        self.switch_1_2hand=(db['Object8'])
        self.switch_bonus_on_shield=(db['Object9'])
        self.switch_bonus_off_shield=(db['Object10'])
        self.switch_shield=(db['Object11'])
        self.switch_bonus_on_Leather=(db['Object12'])
        self.switch_bonus_off_Leather=(db['Object13'])
        self.switch_Leather=(db['Object14'])
        self.switch_bonus_on_Chain=(db['Object15'])
        self.switch_bonus_off_Chain=(db['Object16'])
        self.switch_Chain=(db['Object17'])
        self.switch_bonus_on_Plate=(db['Object18'])
        self.switch_bonus_off_Plate=(db['Object19'])
        self.switch_Plate=(db['Object20'])

