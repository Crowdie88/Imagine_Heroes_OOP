import sys
# import only system from os 
from os import system
# color und styles
from colorama import init, Fore, Back, Style
# sounds
import winsound

def clear():
        _ = system('cls')

class Help():
    def getHelp(self):
        clear()
        print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
        print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
        print("")
        print("")
        print("This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
        print("")
        print("")
        print("Commands for your character:                                          #")
        print("                                                                      #")
        print("Enter:                                                                #")
        print("      'w': to walk towards the north                                  #")
        print("      's': to walk towards the south                                  #")
        print("      'a': to walk towards the west                                   #")
        print("      'd': to walk towards the east                                   #")
        print("      ------------------------------------                            #")
        print("      'q'   : to view your quests                                     #")
        print("      'inv' : to open the inventory                                   #")
        print("      'char': to get a character overview                             #")
        print("      'rest': to regenerate your life points around a campfire        #")
        print("      'map' : to get your coordinates                                 #")
        print("                                                                      #")
        print("In fight: enter the 'SPACE_BUTTON': to get more options               #")
        print("                                                                      #")
        print("Game Commands:                                                        #")
        print("                                                                      #")
        print("      'save': to save the game                                        #")
        print("      'load': to load your last saved game                            #")
        print("      'quit': to exit the game                                        #")
        print("")