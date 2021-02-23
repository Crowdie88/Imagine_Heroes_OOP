# color und styles
from colorama import init, Fore, Back, Style
init(wrap=False)
init(autoreset=True)
# import only system from os 
from os import system, name 

def clear():
        _ = system('cls')

class Skill_Tree():
    #---------------------------------------------------
    def getSkill_Tree(self, player):
        clear()
        print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
        print("")
        print("")
        print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
        print("")
        print(Style.DIM + "This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
        print("")
        print("")
        print(Fore.LIGHTMAGENTA_EX + "You got 1 skill point")
        print("-------------------------------------------------------------------------+")
        print("Skill tree:                                                              |")
        print("                                                                         |")
        print("You have:", player.getSkill_points(), "Skill points left                                            |")
        print("                                                                         |")
        print("Which Skill do you want to learn?                                        |")
        print("                                                                         |")
        print("Armory:                                                                  |")
        print(Fore.LIGHTYELLOW_EX + "         ( 1 ) The Berserker:                                           ","|")
        print(Fore.LIGHTYELLOW_EX + "               If you carry 2x 1-hand weapons, you get a                ","|")
        print(Fore.LIGHTYELLOW_EX + "               bonus of + 3% on the chance for a 2nd attack             ","|")
        print("               [", player.getArmory_counter(),"skill point required ]                                |")
        print("                                                                         |")
        print(Fore.LIGHTRED_EX + "         ( 2 ) The Warrior:                                             ","|")
        print(Fore.LIGHTRED_EX + "               If you carry 1x 2-hand weapon, you get a                 ","|")
        print(Fore.LIGHTRED_EX + "               bonus of + 7% on your total damage                       ","|")
        print("               [", player.getArmory_counter(),"skill point required ]                                |")
        print("                                                                         |")
        print(Fore.LIGHTBLUE_EX + "         ( 3 ) The Defender:                                            ","|")
        print(Fore.LIGHTBLUE_EX + "               If you wear a shield, the required armor points          ","|")
        print(Fore.LIGHTBLUE_EX + "               to absorb damage are reduced by 2                        ","|")
        print("               [", player.getArmory_counter(),"skill point required ]                                |")
        print("                                                                         |")
        print("Passive in fight:                                                                    |")
        print(Fore.LIGHTYELLOW_EX + "         ( 4 ) Evasion:                                                 ","|")
        print(Fore.LIGHTYELLOW_EX + "               Chance of 25% of your dexterity to evade                 ","|")
        print(Fore.LIGHTYELLOW_EX + "               an attack                                                ","|")
        print("               [", player.getPassive_counter(),"skill point required ]                                |")
        print("                                                                         |")
        print(Fore.LIGHTRED_EX + "         ( 5 ) Counterattack:                                           ","|")
        print(Fore.LIGHTRED_EX + "               Chance of 20% of your strength to counter an attack,     ","|")
        print(Fore.LIGHTRED_EX + "               so you only get 50% of the incoming damage and then      ","|")
        print(Fore.LIGHTRED_EX + "               cause 25% of your own damage to the opponent             ","|")
        print("               [", player.getPassive_counter(),"skill point required ]                                |")
        print("                                                                         |")
        print(Fore.LIGHTBLUE_EX + "         ( 6 ) Push Back:                                               ","|")
        print(Fore.LIGHTBLUE_EX + "               When blocking, the damage is thrown back                 ","|")
        print(Fore.LIGHTBLUE_EX + "               to the attacker                                          ","|")
        print("               [", player.getPassive_counter(),"skill point required ]                                |")
        print("                                                                         |")
        print("                                                                         |")
        print("         ( 7 ) Save skill point and go back                              |")
        print("-------------------------------------------------------------------------+")
        while True:
            skill = input("Your choice: ")
            if skill == "1":
                if player.getSkill_points() >= player.getArmory_counter():
                    if player.getThe_Berserker() == False:
                        print("")
                        print(Fore.LIGHTYELLOW_EX + "You have learned the skill 'The Berserker'.")
                        player.setThe_Berserker(True)
                        player.setSkill_points(player.getSkill_points() - player.getArmory_counter())
                        player.setArmory_counter(player.getArmory_counter() + 1)
                        print("")
                        break
                    else:
                        print("")
                        print("You are allready learned this skill, choose another one.")
                        print("")
                else:
                    print("")
                    print("You have not enough skill points left, try another one")
                    print("")
            elif skill == "2":
                if player.getSkill_points() >= player.getArmory_counter():
                    if player.getThe_Warrior() == False:
                        print("")
                        print(Fore.LIGHTRED_EX + "You have learned the skill 'The Warrior'.")
                        player.setThe_Warrior(True)
                        player.setSkill_points(player.getSkill_points() - player.getArmory_counter())
                        player.setArmory_counter(player.getArmory_counter() + 1)
                        print("")
                        break
                    else:
                        print("")
                        print("You are allready learned this skill, choose another one.")
                        print("")
                else:
                    print("")
                    print("You have not enough skill points left, try another one")
                    print("")
            elif skill == "3":
                if player.getSkill_points() >= player.getArmory_counter():
                    if player.getThe_Defender() == False:
                        print("")
                        print(Fore.LIGHTBLUE_EX + "You have learned the skill 'The Defender'.")
                        player.setThe_Defender(True)
                        player.setSkill_points(player.getSkill_points() - player.getArmory_counter())
                        player.setArmory_counter(player.getArmory_counter() + 1)
                        print("")
                        break
                    else:
                        print("")
                        print("You are allready learned this skill, choose another one.")
                        print("")
                else:
                    print("")
                    print("You have not enough skill points left, try another one")
                    print("")
            elif skill == "4":
                if player.getSkill_points() >= player.getPassive_counter():
                    if player.getEvasion_Switch() == False:
                        print("")
                        print(Fore.LIGHTYELLOW_EX + "You have learned the skill 'Evasion'.")
                        player.setEvasion_Switch(True)
                        player.setSkill_points(player.getSkill_points() - player.getPassive_counter())
                        player.setPassive_counter(player.getPassive_counter() + 1)
                        print("")
                        break
                    else:
                        print("")
                        print("You are allready learned this skill, choose another one.")
                        print("")
                else:
                    print("")
                    print("You have not enough skill points left, try another one")
                    print("")
            elif skill == "5":
                if player.getSkill_points() >= player.getPassive_counter():
                    if player.getCounterattack_Switch() == False:
                        print("")
                        print(Fore.LIGHTRED_EX + "You have learned the skill 'Counterattack'.")
                        player.setCounterattack_Switch(True)
                        player.setSkill_points(player.getSkill_points() - player.getPassive_counter())
                        player.setPassive_counter(player.getPassive_counter() + 1)
                        print("")
                        break
                    else:
                        print("")
                        print("You are allready learned this skill, choose another one.")
                        print("")
                else:
                    print("")
                    print("You have not enough skill points left, try another one")
                    print("")
            elif skill == "6":
                if player.getSkill_points() >= player.getPassive_counter():
                    if player.getPush_Back_Switch() == False:
                        print("")
                        print(Fore.LIGHTBLUE_EX + "You have learned the skill 'Push Back'.")
                        player.setPush_Back_Switch(True)
                        player.setSkill_points(player.getSkill_points() - player.getPassive_counter())
                        player.setPassive_counter(player.getPassive_counter() + 1)
                        print("")
                        break
                    else:
                        print("")
                        print("You are allready learned this skill, choose another one.")
                        print("")
                else:
                    print("")
                    print("You have not enough skill points left, try another one")
                    print("")
            elif skill == "7":
                break
            else:
                print("")
                print("Wrong input, try again...")
                print("")