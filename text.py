# import only system from os 
from os import system, name
# sounds
import winsound
# color und styles
from colorama import init, Fore, Back, Style

init(wrap=False)
init(autoreset=True)

def clear():
        _ = system('cls')

def introduction():
    print("")
    print(Fore.YELLOW + "Imagine" + Style.BRIGHT + Fore.GREEN + " Heroes", "who embark on the greatest adventures of their lives in...")
    print("a world full of danger.")
    print("A world full of magical objects.")
    print("A world full of monsters.")
    print("The survival of these heroes decides the fate of thousands.")
    print("You want to become one of them.")
    print("Now go and start your journey in the world of", Fore.YELLOW + "Imagine" + Style.BRIGHT + Fore.GREEN +" Heroes" + Fore.RESET + "!")
    print("")
    print(Fore.LIGHTYELLOW_EX + "Continue...", end='')
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