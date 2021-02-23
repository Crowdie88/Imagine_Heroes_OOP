
import random
import items
import enemys
import player
# sounds
import winsound
# color und styles
from colorama import init, Fore, Back, Style
# import sleep to show output for some time period 
from time import sleep
import sys
# import only system from os 
from os import system
# import sleep to show output for some time period 
def clear():
        _ = system('cls')

class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    def getfight(self):
        clear()
        print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
        print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
        print("")
        print("")
        print("This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
        print("")
        print("")
        enemy_display = True
        if self.enemy is not None:
            winsound.PlaySound("sounds\\kampfanfang.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            sleep(1)
            clear()
            print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
            print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
            print("")
            print("")
            print("This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
            print("")
            print("")
            loop = True
            while loop:
                if enemy_display == True:
                    print("")
                    for (x, i) in enumerate(self.enemy, start=1): 
                        print("(",x,")",Fore.RED + i.Name,"\n       Life: ", i.Lp,"\n       Damage: ", i.MinDmg,"-", i.MaxDmg,"\n       Attacks: ", i.Attacks)
                        print("")
                var1_player_chance = self.player.getAttack2() # player chance attack2
                var2_switch_attack2 = 0 # switch variable attack2
                var3_random_attack2 = random.randint(1,100) # dice attack2
                var4_switch2_attack2 = 0 # switch 2 variable 2 attack2
                print("")
                print("Enter the 'SPACE BAR' to select other options...")
                print(Fore.LIGHTYELLOW_EX + "Which enemy do you attack: ", end="")
                which_enemy = input()
                print("")
                enemy_display = True
                if which_enemy == "1" and len(self.enemy) >= 1:
                    while var2_switch_attack2 < 1:
                        dmg = 0
                        dmg = self.player.getDmg()
                        print("You attack",Fore.RED + self.enemy[0].Name,"at position ( 1 ) and hit him with your attack for",dmg, "damage.")
                        winsound.PlaySound("sounds\\schwert.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                        self.enemy[0].get_hit(dmg, self.player)
                        var2_switch_attack2 += 1
                        if self.enemy[0].Lp > 0:
                            print(Fore.RED + self.enemy[0].Name," at position ( 1 ) has ",Fore.LIGHTGREEN_EX + str(self.enemy[0].Lp), "life points left")
                            print("")
                        if self.enemy[0].Lp <= 0:
                            del self.enemy[0]
                            if len(self.enemy) == 0:
                                return
                        if var3_random_attack2 <= var1_player_chance and var4_switch2_attack2 == 0 and len(self.enemy) >= 1:
                            var2_switch_attack2 = 0
                            var4_switch2_attack2 += 1
                            print(Fore.YELLOW + "You're so skilled in combat that you can succeed in a second attack...")
                            sleep(0.8)
                            print("")
                            pass
                        else:
                            break
                    for (x, i) in enumerate(self.enemy, start=1):
                        dice_block = random.randint(1,100)
                        dice_counterattack = random.randint(1,100)
                        dice_evasion = random.randint(1,100)
                        enemy_dmg = i.getDmg()
                        # Shield -------------------------------------------
                        if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                            if dice_block <= self.player.getBlockchance():
                                if self.player.getPush_Back_Switch() == True:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                    print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                    print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                    i.get_hit(enemy_dmg, self.player)
                                    if i.Lp > 0:
                                        print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                        print("")
                                    if i.Lp <= 0:
                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        sleep(1)
                                        del self.enemy[x-1]
                                        if len(self.enemy) == 0:
                                            return
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                    sleep(1)
                        # Counterattack ---------------------------------
                            elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                    self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                i.get_hit(round(dmg * 0.25), self.player)
                                if i.Lp > 0:
                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                    print("")
                                if i.Lp <= 0:
                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                    sleep(1)
                                    del self.enemy[x-1]
                                    if len(self.enemy) == 0:
                                        return
                                #-------------------------------
                            else:
                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                self.player.get_Hit(enemy_dmg)
                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                sleep(0.2)
                        elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                            print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                            else:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                            print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                            i.get_hit(round(dmg * 0.25), self.player)
                            if i.Lp > 0:
                                print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                print("")
                            if i.Lp <= 0:
                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                sleep(1)
                                del self.enemy[x-1]
                                if len(self.enemy) == 0:
                                    return
                        else:
                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                            else:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                            self.player.get_Hit(enemy_dmg)
                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                            sleep(0.2)
                
    # --------------------------------------------------------------------------------------------------------------------------------------
                elif which_enemy == "2" and len(self.enemy) >= 2:
                    while var2_switch_attack2 < 1:
                        dmg = 0
                        dmg = self.player.getDmg()
                        print("You attack",Fore.RED + self.enemy[1].Name,"at position ( 1 ) and hit him with your attack for",dmg, "damage.")
                        winsound.PlaySound("sounds\\schwert.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                        self.enemy[1].get_hit(dmg, self.player)
                        var2_switch_attack2 += 1
                        if self.enemy[1].Lp > 0:
                            print(Fore.RED + self.enemy[1].Name," at position ( 1 ) has ",Fore.LIGHTGREEN_EX + str(self.enemy[1].Lp), "life points left")
                            print("")
                        if self.enemy[1].Lp <= 0:
                            del self.enemy[1]
                            if len(self.enemy) == 0:
                                return
                        if var3_random_attack2 <= var1_player_chance and var4_switch2_attack2 == 0 and len(self.enemy) >= 1:
                            var2_switch_attack2 = 0
                            var4_switch2_attack2 += 1
                            print(Fore.YELLOW + "You're so skilled in combat that you can succeed in a second attack...")
                            sleep(0.8)
                            print("")
                            pass
                        else:
                            break
                    for (x, i) in enumerate(self.enemy, start=1):
                        dice_block = random.randint(1,100)
                        dice_counterattack = random.randint(1,100)
                        dice_evasion = random.randint(1,100)
                        enemy_dmg = i.getDmg()
                        # Shield -------------------------------------------
                        if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                            if dice_block <= self.player.getBlockchance():
                                if self.player.getPush_Back_Switch() == True:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                    print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                    print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                    i.get_hit(enemy_dmg, self.player)
                                    if i.Lp > 0:
                                        print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                        print("")
                                    if i.Lp <= 0:
                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        sleep(1)
                                        del self.enemy[x-1]
                                        if len(self.enemy) == 0:
                                            return
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                    sleep(1)
                        # Counterattack ---------------------------------
                            elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                    self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                i.get_hit(round(dmg * 0.25), self.player)
                                if i.Lp > 0:
                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                    print("")
                                if i.Lp <= 0:
                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                    sleep(1)
                                    del self.enemy[x-1]
                                    if len(self.enemy) == 0:
                                        return
                                #-------------------------------
                            else:
                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                self.player.get_Hit(enemy_dmg)
                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                sleep(0.2)
                        elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                            print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                            else:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                            print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                            i.get_hit(round(dmg * 0.25), self.player)
                            if i.Lp > 0:
                                print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                print("")
                            if i.Lp <= 0:
                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                sleep(1)
                                del self.enemy[x-1]
                                if len(self.enemy) == 0:
                                    return
                        else:
                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                            else:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                            self.player.get_Hit(enemy_dmg)
                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                            sleep(0.2)
    # --------------------------------------------------------------------------------------------------------------------------------------
                elif which_enemy == "3" and len(self.enemy) >= 3:
                    while var2_switch_attack2 < 1:
                        dmg = 0
                        dmg = self.player.getDmg()
                        print("You attack",Fore.RED + self.enemy[2].Name,"at position ( 1 ) and hit him with your attack for",dmg, "damage.")
                        winsound.PlaySound("sounds\\schwert.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                        self.enemy[2].get_hit(dmg, self.player)
                        var2_switch_attack2 += 1
                        if self.enemy[2].Lp > 0:
                            print(Fore.RED + self.enemy[1].Name," at position ( 1 ) has ",Fore.LIGHTGREEN_EX + str(self.enemy[2].Lp), "life points left")
                            print("")
                        if self.enemy[2].Lp <= 0:
                            del self.enemy[2]
                            if len(self.enemy) == 0:
                                return
                        if var3_random_attack2 <= var1_player_chance and var4_switch2_attack2 == 0 and len(self.enemy) >= 1:
                            var2_switch_attack2 = 0
                            var4_switch2_attack2 += 1
                            print(Fore.YELLOW + "You're so skilled in combat that you can succeed in a second attack...")
                            sleep(0.8)
                            print("")
                            pass
                        else:
                            break
                    for (x, i) in enumerate(self.enemy, start=1):
                        dice_block = random.randint(1,100)
                        dice_counterattack = random.randint(1,100)
                        dice_evasion = random.randint(1,100)
                        enemy_dmg = i.getDmg()
                        # Shield -------------------------------------------
                        if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                            if dice_block <= self.player.getBlockchance():
                                if self.player.getPush_Back_Switch() == True:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                    print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                    print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                    i.get_hit(enemy_dmg, self.player)
                                    if i.Lp > 0:
                                        print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                        print("")
                                    if i.Lp <= 0:
                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        sleep(1)
                                        del self.enemy[x-1]
                                        if len(self.enemy) == 0:
                                            return
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                    sleep(1)
                        # Counterattack ---------------------------------
                            elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                    self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                i.get_hit(round(dmg * 0.25), self.player)
                                if i.Lp > 0:
                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                    print("")
                                if i.Lp <= 0:
                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                    sleep(1)
                                    del self.enemy[x-1]
                                    if len(self.enemy) == 0:
                                        return
                                #-------------------------------
                            else:
                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                else:
                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                self.player.get_Hit(enemy_dmg)
                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                sleep(0.2)
                        elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                            print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                            else:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                            print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                            i.get_hit(round(dmg * 0.25), self.player)
                            if i.Lp > 0:
                                print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                print("")
                            if i.Lp <= 0:
                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                sleep(1)
                                del self.enemy[x-1]
                                if len(self.enemy) == 0:
                                    return
                        else:
                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                            else:
                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                            self.player.get_Hit(enemy_dmg)
                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                            sleep(0.2)
                elif which_enemy == " ":
                    print("")
                    print("Your options are:")
                    print("")
                    print("( 1 ) Drink a potion")
                    print("( 2 ) Trying to escape")
                    print("( 3 ) Back")
                    print("")
                    while True:
                        p_small = False
                        p_small_anzahl = 0
                        p_small_healing = 15
                        p_normal = False
                        p_normal_anzahl = 0
                        p_normal_healing = 35
                        p_big = False
                        p_big_anzahl = 0
                        p_big_healing = 80
                        option = input("Option: ")
                        if option == "1":
                            print("")
                            print("Which Potion Size?")
                            print("")
                            for i in self.player.Inventory:
                                if i.getCategory() == "Potion" and i.getName() == "Small_Potion":
                                    if len(i.getStack()) > 0:
                                        p_small_anzahl = (len(i.getStack()) + 1)
                                        p_small = True
                                        p_small_healing = i.getSize(self.player.getRace())
                                    elif len(i.getStack()) == 0:
                                        p_small_anzahl = 1
                                        p_small = True
                                        p_small_healing = i.getSize(self.player.getRace())
                                if i.getCategory() == "Potion" and i.getName() == "Normal_Potion":
                                    if len(i.getStack()) > 0:
                                        p_normal_anzahl = (len(i.getStack()) + 1)
                                        p_normal = True
                                        p_normal_healing = i.getSize(self.player.getRace())
                                    elif len(i.getStack()) == 0:
                                        p_normal_anzahl = 1
                                        p_normal = True
                                        p_normal_healing = i.getSize(self.player.getRace())
                                if i.getCategory() == "Potion" and i.getName() == "Big_Potion":
                                    if len(i.getStack()) > 0:
                                        p_big_anzahl = (len(i.getStack()) + 1)
                                        p_big = True
                                        p_big_healing = i.getSize(self.player.getRace())
                                    elif len(i.getStack()) == 0:
                                        p_big_anzahl = 1
                                        p_big = True
                                        p_big_healing = i.getSize(self.player.getRace())
                            if p_small == True:
                                print("( 1 ) Small_Potion, ", "Quantity:", p_small_anzahl, " Healing:", p_small_healing)
                            else:
                                print("( 1 ) Small_Potion, ", "Quantity:", "0", " Healing:", p_small_healing)
                            if p_normal == True:
                                print("( 2 ) Normal_Potion, ", "Quantity:", p_normal_anzahl, " Healing:", p_normal_healing)
                            else:
                                print("( 2 ) Normal_Potion, ", "Quantity:", "0", " Healing:", p_normal_healing)
                            if p_big == True:
                                print("( 3 ) Big_Potion, ", "Quantity:", p_big_anzahl, " Healing:", p_big_healing)
                            else:
                                print("( 3 ) Big_Potion, ", "Quantity:", "0", " Healing:", p_big_healing)
                            print("( 4 ) Back")
                            print("")
                            while True:
                                small = False
                                normal = False
                                big = False
                                choose_potion = input("Option: ")
                                if choose_potion == "1":
                                    for (x, i) in enumerate(self.player.Inventory, start=1):
                                        if i.getCategory() == "Potion" and i.getName() == "Small_Potion":
                                            if len(i.getStack()) > 0:
                                                if self.player.getHealth() <= (self.player.getMaxHealth() - i.getSize(self.player.getRace())):
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(i.getSize(self.player.getRace())) + " life points")
                                                    self.player.setHealth(self.player.getHealth() + i.getSize(self.player.getRace()))
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del i.getStack()[0]
                                                    small = True
                                                    break
                                                elif self.player.getHealth() > (self.player.getMaxHealth() - i.getSize(self.player.getRace())) and self.player.getHealth() < self.player.getMaxHealth():
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(self.player.getMaxHealth() - self.player.getHealth()) + " life points")
                                                    self.player.setHealth(self.player.getMaxHealth())
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del i.getStack()[0]
                                                    small = True
                                                    break
                                                else:
                                                    print("")
                                                    print(Fore.GREEN + "Your life points are already full")
                                                    print("")
                                                    small = True
                                                    break
                                            elif len(i.getStack()) == 0:
                                                if self.player.getHealth() <= (self.player.getMaxHealth() - i.getSize(self.player.getRace())):
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(i.getSize(self.player.getRace())) + " life points")
                                                    self.player.setHealth(self.player.getHealth() + i.getSize(self.player.getRace()))
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del self.player.Inventory[x-1]
                                                    small = True
                                                    break
                                                elif self.player.getHealth() > (self.player.getMaxHealth() - i.getSize(self.player.getRace())) and self.player.getHealth() < self.player.getMaxHealth():
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(self.player.getMaxHealth() - self.player.getHealth()) + " life points")
                                                    self.player.setHealth(self.player.getMaxHealth())
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del self.player.Inventory[x-1]
                                                    small = True
                                                    break
                                                else:
                                                    print("")
                                                    print(Fore.GREEN + "Your life points are already full")
                                                    print("")
                                                    small = True
                                                    break
                                    if small == False:
                                        print("")
                                        print(Fore.RED + "You have no small healing potions in your inventory")
                                        print("")
                                        break
                                    else:    
                                        for (x, i) in enumerate(self.enemy, start=1):
                                            dice_block = random.randint(1,100)
                                            dice_counterattack = random.randint(1,100)
                                            dice_evasion = random.randint(1,100)
                                            enemy_dmg = i.getDmg()
                                            # Shield -------------------------------------------
                                            if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                                                if dice_block <= self.player.getBlockchance():
                                                    if self.player.getPush_Back_Switch() == True:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                        print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                                        print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                                        i.get_hit(enemy_dmg, self.player)
                                                        if i.Lp > 0:
                                                            print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                            print("")
                                                        if i.Lp <= 0:
                                                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                            winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                            sleep(1)
                                                            del self.enemy[x-1]
                                                            if len(self.enemy) == 0:
                                                                return
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                        sleep(1)
                                            # Counterattack ---------------------------------
                                                elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                                    if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                        self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                                    print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                                    i.get_hit(round(dmg * 0.25), self.player)
                                                    if i.Lp > 0:
                                                        print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                        print("")
                                                    if i.Lp <= 0:
                                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                        sleep(1)
                                                        del self.enemy[x-1]
                                                        if len(self.enemy) == 0:
                                                            return
                                                    #-------------------------------
                                                else:
                                                    if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                                    self.player.get_Hit(enemy_dmg)
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    sleep(0.2)
                                            elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                else:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                    self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                                print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                                i.get_hit(round(dmg * 0.25), self.player)
                                                if i.Lp > 0:
                                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                    print("")
                                                if i.Lp <= 0:
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    sleep(1)
                                                    del self.enemy[x-1]
                                                    if len(self.enemy) == 0:
                                                        return
                                            else:
                                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                else:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                                self.player.get_Hit(enemy_dmg)
                                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                sleep(0.2)
                                        break
                                elif choose_potion == "2":
                                    for (x, i) in enumerate(self.player.Inventory, start=1):
                                        if i.getCategory() == "Potion" and i.getName() == "Normal_Potion":
                                            if len(i.getStack()) > 0:
                                                if self.player.getHealth() <= (self.player.getMaxHealth() - i.getSize(self.player.getRace())):
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(i.getSize(self.player.getRace())) + " life points")
                                                    self.player.setHealth(self.player.getHealth() + i.getSize(self.player.getRace()))
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del i.getStack()[0]
                                                    normal = True
                                                    break
                                                elif self.player.getHealth() > (self.player.getMaxHealth() - i.getSize(self.player.getRace())) and self.player.getHealth() < self.player.getMaxHealth():
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(self.player.getMaxHealth() - self.player.getHealth()) + " life points")
                                                    self.player.setHealth(self.player.getMaxHealth())
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del i.getStack()[0]
                                                    normal = True
                                                    break
                                                else:
                                                    print("")
                                                    print(Fore.GREEN + "Your life points are already full")
                                                    print("")
                                                    normal = True
                                                    break
                                            elif len(i.getStack()) == 0:
                                                if self.player.getHealth() <= (self.player.getMaxHealth() - i.getSize(self.player.getRace())):
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(i.getSize(self.player.getRace())) + " life points")
                                                    self.player.setHealth(self.player.getHealth() + i.getSize(self.player.getRace()))
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del self.player.Inventory[x-1]
                                                    normal = True
                                                    break
                                                elif self.player.getHealth() > (self.player.getMaxHealth() - i.getSize(self.player.getRace())) and self.player.getHealth() < self.player.getMaxHealth():
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(self.player.getMaxHealth() - self.player.getHealth()) + " life points")
                                                    self.player.setHealth(self.player.getMaxHealth())
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del self.player.Inventory[x-1]
                                                    normal = True
                                                    break
                                                else:
                                                    print("")
                                                    print(Fore.GREEN + "Your life points are already full")
                                                    print("")
                                                    normal = True
                                                    break
                                    if normal == False:
                                        print("")
                                        print(Fore.RED + "You have no normal healing potions in your inventory")
                                        print("")
                                        break
                                    else:    
                                        for (x, i) in enumerate(self.enemy, start=1):
                                            dice_block = random.randint(1,100)
                                            dice_counterattack = random.randint(1,100)
                                            dice_evasion = random.randint(1,100)
                                            enemy_dmg = i.getDmg()
                                            # Shield -------------------------------------------
                                            if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                                                if dice_block <= self.player.getBlockchance():
                                                    if self.player.getPush_Back_Switch() == True:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                        print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                                        print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                                        i.get_hit(enemy_dmg, self.player)
                                                        if i.Lp > 0:
                                                            print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                            print("")
                                                        if i.Lp <= 0:
                                                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                            winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                            sleep(1)
                                                            del self.enemy[x-1]
                                                            if len(self.enemy) == 0:
                                                                return
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                        sleep(1)
                                            # Counterattack ---------------------------------
                                                elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                                    if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                        self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                                    print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                                    i.get_hit(round(dmg * 0.25), self.player)
                                                    if i.Lp > 0:
                                                        print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                        print("")
                                                    if i.Lp <= 0:
                                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                        sleep(1)
                                                        del self.enemy[x-1]
                                                        if len(self.enemy) == 0:
                                                            return
                                                    #-------------------------------
                                                else:
                                                    if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                                    self.player.get_Hit(enemy_dmg)
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    sleep(0.2)
                                            elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                else:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                    self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                                print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                                i.get_hit(round(dmg * 0.25), self.player)
                                                if i.Lp > 0:
                                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                    print("")
                                                if i.Lp <= 0:
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    sleep(1)
                                                    del self.enemy[x-1]
                                                    if len(self.enemy) == 0:
                                                        return
                                            else:
                                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                else:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                                self.player.get_Hit(enemy_dmg)
                                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                sleep(0.2)
                                        break
                                elif choose_potion == "3":
                                    for (x, i) in enumerate(self.player.Inventory, start=1):
                                        if i.getCategory() == "Potion" and i.getName() == "Big_Potion":
                                            if len(i.getStack()) > 0:
                                                if self.player.getHealth() <= (self.player.getMaxHealth() - i.getSize(self.player.getRace())):
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(i.getSize(self.player.getRace())) + " life points")
                                                    self.player.setHealth(self.player.getHealth() + i.getSize(self.player.getRace()))
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del i.getStack()[0]
                                                    big = True
                                                    break
                                                elif self.player.getHealth() > (self.player.getMaxHealth() - i.getSize(self.player.getRace())) and self.player.getHealth() < self.player.getMaxHealth():
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(self.player.getMaxHealth() - self.player.getHealth()) + " life points")
                                                    self.player.setHealth(self.player.getMaxHealth())
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del i.getStack()[0]
                                                    big = True
                                                    break
                                                else:
                                                    print("")
                                                    print(Fore.GREEN + "Your life points are already full")
                                                    print("")
                                                    big = True
                                                    break
                                            elif len(i.getStack()) == 0:
                                                if self.player.getHealth() <= (self.player.getMaxHealth() - i.getSize(self.player.getRace())):
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(i.getSize(self.player.getRace())) + " life points")
                                                    self.player.setHealth(self.player.getHealth() + i.getSize(self.player.getRace()))
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del self.player.Inventory[x-1]
                                                    big = True
                                                    break
                                                elif self.player.getHealth() > (self.player.getMaxHealth() - i.getSize(self.player.getRace())) and self.player.getHealth() < self.player.getMaxHealth():
                                                    winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    print("")
                                                    print(Fore.GREEN + "You regenerate " + str(self.player.getMaxHealth() - self.player.getHealth()) + " life points")
                                                    self.player.setHealth(self.player.getMaxHealth())
                                                    print("Yor actually Lifepoints are:", Fore.GREEN + str(self.player.getHealth()))
                                                    print("")
                                                    del self.player.Inventory[x-1]
                                                    big = True
                                                    break
                                                else:
                                                    print("")
                                                    print(Fore.GREEN + "Your life points are already full")
                                                    print("")
                                                    big = True
                                                    break
                                    if big == False:
                                        print("")
                                        print(Fore.RED + "You have no big healing potions in your inventory")
                                        print("")
                                        break
                                    else:    
                                        for (x, i) in enumerate(self.enemy, start=1):
                                            dice_block = random.randint(1,100)
                                            dice_counterattack = random.randint(1,100)
                                            dice_evasion = random.randint(1,100)
                                            enemy_dmg = i.getDmg()
                                            # Shield -------------------------------------------
                                            if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                                                if dice_block <= self.player.getBlockchance():
                                                    if self.player.getPush_Back_Switch() == True:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                        print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                                        print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                                        i.get_hit(enemy_dmg, self.player)
                                                        if i.Lp > 0:
                                                            print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                            print("")
                                                        if i.Lp <= 0:
                                                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                            winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                            sleep(1)
                                                            del self.enemy[x-1]
                                                            if len(self.enemy) == 0:
                                                                return
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                        sleep(1)
                                            # Counterattack ---------------------------------
                                                elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                                    if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                        self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                                    print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                                    i.get_hit(round(dmg * 0.25), self.player)
                                                    if i.Lp > 0:
                                                        print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                        print("")
                                                    if i.Lp <= 0:
                                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                        winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                        sleep(1)
                                                        del self.enemy[x-1]
                                                        if len(self.enemy) == 0:
                                                            return
                                                    #-------------------------------
                                                else:
                                                    if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                    else:
                                                        print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                                    self.player.get_Hit(enemy_dmg)
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    sleep(0.2)
                                            elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                else:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                    self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                                print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                                i.get_hit(round(dmg * 0.25), self.player)
                                                if i.Lp > 0:
                                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                    print("")
                                                if i.Lp <= 0:
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    sleep(1)
                                                    del self.enemy[x-1]
                                                    if len(self.enemy) == 0:
                                                        return
                                            else:
                                                if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                                else:
                                                    print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                                self.player.get_Hit(enemy_dmg)
                                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                sleep(0.2)
                                        break
                                if choose_potion == "4":
                                    break
                                else:
                                    print("")
                                    print("Wrong input, try again...")
                                    print("")
                            break
                        elif option == "2":
                            run = random.randint(1,6)
                            if run <= self.player.getEscape():
                                winsound.PlaySound("sounds\\chicken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                clear()
                                print(Fore.YELLOW + "          ||  ||\\\\      //||    //  \\\\      //#####   ||  ||\\\\     ||  ||######\n          ||  || \\\\    // ||   //    \\\\    //         ||  || \\\\    ||  ||\n          ||  ||  \\\\  //  ||  //######\\\\  //          ||  ||  \\\\   ||  ||######\n          ||  ||   \\\\//   ||  ||      ||  ||   ###||  ||  ||   \\\\  ||  ||\n          ||  ||          ||  ||      ||  ||      ||  ||  ||    \\\\ ||  ||\n          ||  ||          ||  ||      ||  ||######||  ||  ||     \\\\||  ||######")
                                print("")
                                print("")
                                print(Style.BRIGHT + Fore.GREEN + "                    ||      ||  ||######  ||#####||  ||######||  ||######  ######\n                    ||      ||  ||        ||     ||  ||      ||  ||        ||\n                    ||######||  ||######  ||#####||  ||      ||  ||######  ######\n                    ||      ||  ||        ||  \\\\     ||      ||  ||            ||\n                    ||      ||  ||        ||   \\\\    ||      ||  ||            ||\n                    ||      ||  ||######  ||    \\\\   ||######||  ||######  ######")
                                print("")
                                print(Style.DIM + "This Game is produced by Jens Tucholski (usebtc88@gmail.com)")
                                print("")
                                print("")
                                print("")
                                print(Fore.LIGHTYELLOW_EX + "You did it, you run away like a chicken.")
                                loop = False
                            else:
                                print("")
                                print(Fore.LIGHTMAGENTA_EX + "Unfortunately the escape was unsuccessful...")
                                print(Fore.LIGHTMAGENTA_EX + "The enemys are angry...")
                                print("")
                                for (x, i) in enumerate(self.enemy, start=1):
                                    dice_block = random.randint(1,100)
                                    dice_counterattack = random.randint(1,100)
                                    dice_evasion = random.randint(1,100)
                                    enemy_dmg = i.getDmg()
                                    # Shield -------------------------------------------
                                    if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getType() == "Shield":
                                        if dice_block <= self.player.getBlockchance():
                                            if self.player.getPush_Back_Switch() == True:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                print("You are strong enough to divert the attack on", Fore.RED + i.Name, "(",x,")")
                                                print(Fore.RED + i.Name, "(",x,")", "deals", str(enemy_dmg) ,"damage to itself")
                                                i.get_hit(enemy_dmg, self.player)
                                                if i.Lp > 0:
                                                    print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                    print("")
                                                if i.Lp <= 0:
                                                    print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                    winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                    sleep(1)
                                                    del self.enemy[x-1]
                                                    if len(self.enemy) == 0:
                                                        return
                                            else:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you, but you were able to", Fore.LIGHTBLUE_EX + "block","the damage with your shield")
                                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                sleep(1)
                                    # Counterattack ---------------------------------
                                        elif dice_block > self.player.getBlockchance() and dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                            print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                            else:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                                self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                            print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                            i.get_hit(round(dmg * 0.25), self.player)
                                            if i.Lp > 0:
                                                print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                                print("")
                                            if i.Lp <= 0:
                                                print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                                winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                                sleep(1)
                                                del self.enemy[x-1]
                                                if len(self.enemy) == 0:
                                                    return
                                            #-------------------------------
                                        else:
                                            if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                            else:
                                                print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                            self.player.get_Hit(enemy_dmg)
                                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                            sleep(0.2)
                                    elif dice_counterattack <= self.player.getCounterattack() and self.player.getCounterattack_Switch() == True:
                                        print(Fore.RED + i.Name, "(",x,")", "attacks you, but you could foresee his next move and", Fore.LIGHTYELLOW_EX + "counter","his attack.")
                                        if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                            print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                        else:
                                            print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(round((enemy_dmg - self.player.getReduction(self.player.getReductionBonus())* 0.5))), "damage")
                                            self.player.setHealth(self.player.getHealth() - round(enemy_dmg - self.player.getReduction(self.player.getReductionBonus()) * 0.5))
                                        print("You attack", Fore.RED + i.Name, "(",x,") for", round(dmg * 0.25))
                                        i.get_hit(round(dmg * 0.25), self.player)
                                        if i.Lp > 0:
                                            print(Fore.RED + i.Name,"(",x,")"," has ",Fore.LIGHTGREEN_EX + str(i.Lp), "life points left")
                                            print("")
                                        if i.Lp <= 0:
                                            print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                            winsound.PlaySound("sounds\\blocken.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                            sleep(1)
                                            del self.enemy[x-1]
                                            if len(self.enemy) == 0:
                                                return
                                    else:
                                        if enemy_dmg < self.player.getReduction(self.player.getReductionBonus()):
                                            print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(0), "damage")
                                        else:
                                            print(Fore.RED + i.Name, "(",x,")", "attacks you and deals you", Fore.RED + str(enemy_dmg - self.player.getReduction(self.player.getReductionBonus())), "damage")
                                        self.player.get_Hit(enemy_dmg)
                                        print("You have", Fore.GREEN + str(round(self.player.getHealth(), 0)), "lifepoints left")
                                        sleep(0.2)
                            break
                        elif option == "3":
                            break
                        else:
                            print("")
                            print("Wrong input, try again...")
                            print("")
    # --------------------------------------------------------------------------------------------------------------------------------------
                else:
                    print("Wrong input, try again...")
                    enemy_display = False
                        
        else:
            pass
