# color und styles
from colorama import init, Fore, Back, Style
init(wrap=False)
init(autoreset=True)
# import only system from os 
from os import system, name 

def clear():
        _ = system('cls')

class Skills():
    def getSkills(self, player):
        clear()
        print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
        print("")
        print("")
        print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
        print("")
        print(Style.DIM + "This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
        print("")
        print("")
        print("Your Skills:")
        print("")
        print("Armory:")
        print("--------------------")
        if player.getThe_Berserker() == True:
            print("You learned the skill: [", Fore.LIGHTYELLOW_EX + "The Berserker","]")
            print(Fore.LIGHTYELLOW_EX + "                        If you carry 2x 1-hand weapons, you get a")
            print(Fore.LIGHTYELLOW_EX + "                        bonus of + 3% on the chance for a 2nd attack")
        if player.getThe_Warrior() == True:
            print("You learned the skill: [", Fore.LIGHTRED_EX + "The Warrior","]")
            print(Fore.LIGHTRED_EX + "                        If you carry 1x 2-hand weapon, you get a")
            print(Fore.LIGHTRED_EX + "                        bonus of + 7% on your total damage")
        if player.getThe_Defender() == True:
            print("You learned the skill: [", Fore.LIGHTBLUE_EX + "The Defender","]")
            print(Fore.LIGHTBLUE_EX + "                        If you wear a shield, the required armor points")
            print(Fore.LIGHTBLUE_EX + "                        to absorb damage are reduced by 2")


