# sound
import winsound
# import only system from os 
from os import system, name
# color und styles
from colorama import init, Fore, Back, Style

init(wrap=False)
init(autoreset=True)

def clear():
        _ = system('cls')

class C:
    def __init__(self):
        self.bob = ""
    def lear(self):
        print("")
        print(Fore.GREEN + "Continue...", end="")
        input()
        winsound.PlaySound("sounds\\thunder.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        clear()
        print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
        print("")
        print("")
        print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
        print("")
        print(Style.DIM + "This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
        print("")
        print("")