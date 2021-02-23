# color und styles
from colorama import init, Fore, Back, Style
import math
import maps

init(wrap=False)
init(autoreset=True)

class Char:
    def __init__(self, player):
        self.player = player
    def getchar_info(self, strength_bonus):
        if len(self.player.getHead()) == 1 and len(self.player.getBody()) == 1 and len(self.player.getLegs()) == 1 and len(self.player.getFeet()) == 1 and self.player.getHead()[0].getMaterial() == "Leather" and self.player.getBody()[0].getMaterial() == "Leather" and self.player.getLegs()[0].getMaterial() == "Leather" and self.player.getFeet()[0].getMaterial() == "Leather":
            print("")
            print("----------------------------------------------------")
            print(Fore.LIGHTYELLOW_EX + "Armor: Leather, Bonus: + 5% 2nd attack")
            print("----------------------------------------------------")
        elif len(self.player.getHead()) == 1 and len(self.player.getBody()) == 1 and len(self.player.getLegs()) == 1 and len(self.player.getFeet()) == 1 and self.player.getHead()[0].getMaterial() == "Chain" and self.player.getBody()[0].getMaterial() == "Chain" and self.player.getLegs()[0].getMaterial() == "Chain" and self.player.getFeet()[0].getMaterial() == "Chain":
            print("")
            print("----------------------------------------------------")
            print(Fore.LIGHTRED_EX + "Armor: Chain, Bonus: + 8% total damage")
            print("----------------------------------------------------")
        elif len(self.player.getHead()) == 1 and len(self.player.getBody()) == 1 and len(self.player.getLegs()) == 1 and len(self.player.getFeet()) == 1 and self.player.getHead()[0].getMaterial() == "Plate" and self.player.getBody()[0].getMaterial() == "Plate" and self.player.getLegs()[0].getMaterial() == "Plate" and self.player.getFeet()[0].getMaterial() == "Plate":
            print("")
            print("----------------------------------------------------")
            print(Fore.LIGHTBLUE_EX + "Armor: Plate, Bonus: - 1 armor point needed to get dmg reduction, + 2% blockchance")
            print("----------------------------------------------------")
        else:
            print("")
            print("----------------------------------------------------")
            print("Armor:")
            print("----------------------------------------------------")
        if len(self.player.getHead()) == 1:
            # Nothing-----------------------------------------------------------------------------
            if self.player.getHead()[0].getBonus() == 0:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            # Head 1 Bonus-------------------------------------------------------------------------------------------------------------
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 1 and self.player.getHead()[0].getBonus2() == 0:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Vitality +", self.player.getHead()[0].getBonus(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 2 and self.player.getHead()[0].getBonus2() == 0:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Dexterity +", self.player.getHead()[0].getBonus(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 3 and self.player.getHead()[0].getBonus2() == 0:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Strength +", self.player.getHead()[0].getBonus(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            # Head 2 Bonus-----------------------------------------------------------------------------------------------------------
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 1 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 1:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Vitality +", self.player.getHead()[0].getBonus(), "  Vitality +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 1 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 2:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Vitality +", self.player.getHead()[0].getBonus(), "  Dexterity +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 1 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 3:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Vitality +", self.player.getHead()[0].getBonus(), "  Strength +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 2 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 1:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Dexterity +", self.player.getHead()[0].getBonus(), "  Vitality +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 3 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 1:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Strength +", self.player.getHead()[0].getBonus(), "  Vitality +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 2 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 2:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Dexterity +", self.player.getHead()[0].getBonus(), "  Dexterity +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 3 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 3:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Strength +", self.player.getHead()[0].getBonus(), "  Strength +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 2 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 3:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Dexterity +", self.player.getHead()[0].getBonus(), "  Strength +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
            elif self.player.getHead()[0].getBonus() > 0 and self.player.getHead()[0].getAttribute() == 3 and self.player.getHead()[0].getBonus2() > 0 and self.player.getHead()[0].getAttribute2() == 2:
                print("Headgear:      ", self.player.getHead()[0].getType(), "", "Armor:", self.player.getHead()[0].getArmor(), "  Strength +", self.player.getHead()[0].getBonus(), "  Dexterity +", self.player.getHead()[0].getBonus2(), "  Value:", self.player.getHead()[0].getValue(), "Taler")
        else:
            print("Headgear:      empty")
    ##################################################################################################################
        if len(self.player.getBody()) == 1:
            # Nothing-----------------------------------------------------------------------------
            if self.player.getBody()[0].getBonus() == 0:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            # Body 1 Bonus-------------------------------------------------------------------------------------------------------------
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 1 and self.player.getBody()[0].getBonus2() == 0:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Vitality +", self.player.getBody()[0].getBonus(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 2 and self.player.getBody()[0].getBonus2() == 0:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Dexterity +", self.player.getBody()[0].getBonus(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 3 and self.player.getBody()[0].getBonus2() == 0:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Strength +", self.player.getBody()[0].getBonus(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            # Body 2 Bonus-----------------------------------------------------------------------------------------------------------
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 1 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 1:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Vitality +", self.player.getBody()[0].getBonus(), "  Vitality +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 1 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 2:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Vitality +", self.player.getBody()[0].getBonus(), "  Dexterity +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 1 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 3:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Vitality +", self.player.getBody()[0].getBonus(), "  Strength +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 2 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 1:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Dexterity +", self.player.getBody()[0].getBonus(), "  Vitality +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 3 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 1:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Strength +", self.player.getBody()[0].getBonus(), "  Vitality +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 2 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 2:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Dexterity +", self.player.getBody()[0].getBonus(), "  Dexterity +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 3 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 3:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Strength +", self.player.getBody()[0].getBonus(), "  Strength +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 2 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 3:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Dexterity +", self.player.getBody()[0].getBonus(), "  Strength +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
            elif self.player.getBody()[0].getBonus() > 0 and self.player.getBody()[0].getAttribute() == 3 and self.player.getBody()[0].getBonus2() > 0 and self.player.getBody()[0].getAttribute2() == 2:
                print("Chest:         ", self.player.getBody()[0].getType(), "", "Armor:", self.player.getBody()[0].getArmor(), "  Strength +", self.player.getBody()[0].getBonus(), "  Dexterity +", self.player.getBody()[0].getBonus2(), "  Value:", self.player.getBody()[0].getValue(), "Taler")
        else:
            print("Chest:         empty")
    ###############################################################################################################################
        if len(self.player.getLegs()) == 1:
            # Nothing-----------------------------------------------------------------------------
            if self.player.getLegs()[0].getBonus() == 0:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            # Legs 1 Bonus-------------------------------------------------------------------------------------------------------------
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 1 and self.player.getLegs()[0].getBonus2() == 0:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Vitality +", self.player.getLegs()[0].getBonus(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 2 and self.player.getLegs()[0].getBonus2() == 0:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Dexterity +", self.player.getLegs()[0].getBonus(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 3 and self.player.getLegs()[0].getBonus2() == 0:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Strength +", self.player.getLegs()[0].getBonus(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            # Legs 2 Bonus-----------------------------------------------------------------------------------------------------------
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 1 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 1:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Vitality +", self.player.getLegs()[0].getBonus(), "  Vitality +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 1 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 2:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Vitality +", self.player.getLegs()[0].getBonus(), "  Dexterity +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 1 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 3:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Vitality +", self.player.getLegs()[0].getBonus(), "  Strength +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 2 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 1:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Dexterity +", self.player.getLegs()[0].getBonus(), "  Vitality +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 3 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 1:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Strength +", self.player.getLegs()[0].getBonus(), "  Vitality +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 2 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 2:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Dexterity +", self.player.getLegs()[0].getBonus(), "  Dexterity +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 3 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 3:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Strength +", self.player.getLegs()[0].getBonus(), "  Strength +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 2 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 3:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Dexterity +", self.player.getLegs()[0].getBonus(), "  Strength +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
            elif self.player.getLegs()[0].getBonus() > 0 and self.player.getLegs()[0].getAttribute() == 3 and self.player.getLegs()[0].getBonus2() > 0 and self.player.getLegs()[0].getAttribute2() == 2:
                print("Legs:          ", self.player.getLegs()[0].getType(), "", "Armor:", self.player.getLegs()[0].getArmor(), "  Strength +", self.player.getLegs()[0].getBonus(), "  Dexterity +", self.player.getLegs()[0].getBonus2(), "  Value:", self.player.getLegs()[0].getValue(), "Taler")
        else:
            print("Legs:          empty")
    ##########################################################################################################################
        if len(self.player.getFeet()) == 1:
            # Nothing-----------------------------------------------------------------------------
            if self.player.getFeet()[0].getBonus() == 0:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            # Feet 1 Bonus-------------------------------------------------------------------------------------------------------------
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 1 and self.player.getFeet()[0].getBonus2() == 0:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Vitality +", self.player.getFeet()[0].getBonus(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 2 and self.player.getFeet()[0].getBonus2() == 0:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Dexterity +", self.player.getFeet()[0].getBonus(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 3 and self.player.getFeet()[0].getBonus2() == 0:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Strength +", self.player.getFeet()[0].getBonus(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            # Feet 2 Bonus-----------------------------------------------------------------------------------------------------------
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 1 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 1:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Vitality +", self.player.getFeet()[0].getBonus(), "  Vitality +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 1 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 2:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Vitality +", self.player.getFeet()[0].getBonus(), "  Dexterity +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 1 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 3:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Vitality +", self.player.getFeet()[0].getBonus(), "  Strength +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 2 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 1:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Dexterity +", self.player.getFeet()[0].getBonus(), "  Vitality +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 3 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 1:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Strength +", self.player.getFeet()[0].getBonus(), "  Vitality +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 2 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 2:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Dexterity +", self.player.getFeet()[0].getBonus(), "  Dexterity +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            #----------------------------------------------------------------------
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 3 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 3:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Strength +", self.player.getFeet()[0].getBonus(), "  Strength +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 2 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 3:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Dexterity +", self.player.getFeet()[0].getBonus(), "  Strength +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
            elif self.player.getFeet()[0].getBonus() > 0 and self.player.getFeet()[0].getAttribute() == 3 and self.player.getFeet()[0].getBonus2() > 0 and self.player.getFeet()[0].getAttribute2() == 2:
                print("Feet:          ", self.player.getFeet()[0].getType(), "", "Armor:", self.player.getFeet()[0].getArmor(), "  Strength +", self.player.getFeet()[0].getBonus(), "  Dexterity +", self.player.getFeet()[0].getBonus2(), "  Value:", self.player.getFeet()[0].getValue(), "Taler")
        else:
            print("Feet:          empty")
    ##################################################################################################################################
        print("")
        print("----------------------------------------------------")
        print("Jewellery:")
        print("----------------------------------------------------")
        if len(self.player.getEar_Left()) == 1:
            # Ear_Left 1 Bonus-----------------------------------------------------------------------------------------------------------
            if self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 1 and self.player.getEar_Left()[0].getBonus2() == 0:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Vitality +", self.player.getEar_Left()[0].getBonus(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 2 and self.player.getEar_Left()[0].getBonus2() == 0:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Dexterity +", self.player.getEar_Left()[0].getBonus(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 3 and self.player.getEar_Left()[0].getBonus2() == 0:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Strength +", self.player.getEar_Left()[0].getBonus(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            # Ear_Left 2 Bonus------------------------------------------------------------------------------------------------------------ 
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 1 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 1:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Vitality +", self.player.getEar_Left()[0].getBonus(), "  Vitality +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 1 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 2:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Vitality +", self.player.getEar_Left()[0].getBonus(), "  Dexterity +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 1 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 3:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Vitality +", self.player.getEar_Left()[0].getBonus(), "  Strength +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 2 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 1:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Dexterity +", self.player.getEar_Left()[0].getBonus(), "  Vitality +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 3 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 1:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Strength +", self.player.getEar_Left()[0].getBonus(), "  Vitality +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 2 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 2:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Dexterity +", self.player.getEar_Left()[0].getBonus(), "  Dexterity +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 3 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 3:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Strength +", self.player.getEar_Left()[0].getBonus(), "  Strength +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 2 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 3:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Dexterity +", self.player.getEar_Left()[0].getBonus(), "  Strength +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
            elif self.player.getEar_Left()[0].getBonus() > 0 and self.player.getEar_Left()[0].getAttribute() == 3 and self.player.getEar_Left()[0].getBonus2() > 0 and self.player.getEar_Left()[0].getAttribute2() == 2:
                print("Ear_Left:      ", self.player.getEar_Left()[0].getType(), "", " Strength +", self.player.getEar_Left()[0].getBonus(), "  Dexterity +", self.player.getEar_Left()[0].getBonus2(), "  Value:", self.player.getEar_Left()[0].getValue(), "Taler")
        else:
            print("Ear_Left:       empty")
        ########################################################################################################################
        if len(self.player.getEar_Right()) == 1:
            # Ear_Right 1 Bonus-----------------------------------------------------------------------------------------------------------
            if self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 1 and self.player.getEar_Right()[0].getBonus2() == 0:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Vitality +", self.player.getEar_Right()[0].getBonus(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 2 and self.player.getEar_Right()[0].getBonus2() == 0:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Dexterity +", self.player.getEar_Right()[0].getBonus(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 3 and self.player.getEar_Right()[0].getBonus2() == 0:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Strength +", self.player.getEar_Right()[0].getBonus(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            # Ear_Right 2 Bonus------------------------------------------------------------------------------------------------------------ 
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 1 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 1:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Vitality +", self.player.getEar_Right()[0].getBonus(), "  Vitality +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 1 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 2:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Vitality +", self.player.getEar_Right()[0].getBonus(), "  Dexterity +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 1 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 3:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Vitality +", self.player.getEar_Right()[0].getBonus(), "  Strength +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 2 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 1:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Dexterity +", self.player.getEar_Right()[0].getBonus(), "  Vitality +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 3 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 1:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Strength +", self.player.getEar_Right()[0].getBonus(), "  Vitality +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 2 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 2:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Dexterity +", self.player.getEar_Right()[0].getBonus(), "  Dexterity +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 3 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 3:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Strength +", self.player.getEar_Right()[0].getBonus(), "  Strength +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 2 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 3:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Dexterity +", self.player.getEar_Right()[0].getBonus(), "  Strength +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
            elif self.player.getEar_Right()[0].getBonus() > 0 and self.player.getEar_Right()[0].getAttribute() == 3 and self.player.getEar_Right()[0].getBonus2() > 0 and self.player.getEar_Right()[0].getAttribute2() == 2:
                print("Ear_Right:     ", self.player.getEar_Right()[0].getType(), "", " Strength +", self.player.getEar_Right()[0].getBonus(), "  Dexterity +", self.player.getEar_Right()[0].getBonus2(), "  Value:", self.player.getEar_Right()[0].getValue(), "Taler")
        else:
            print("Ear_Right:      empty")
        #############################################################################################################################
        if len(self.player.getFinger_Left()) == 1:
            # Finger_Left 1 Bonus-----------------------------------------------------------------------------------------------------------
            if self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 1 and self.player.getFinger_Left()[0].getBonus2() == 0:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Vitality +", self.player.getFinger_Left()[0].getBonus(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 2 and self.player.getFinger_Left()[0].getBonus2() == 0:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Dexterity +", self.player.getFinger_Left()[0].getBonus(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 3 and self.player.getFinger_Left()[0].getBonus2() == 0:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Strength +", self.player.getFinger_Left()[0].getBonus(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            # Finger_Left 2 Bonus------------------------------------------------------------------------------------------------------------ 
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 1 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 1:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Vitality +", self.player.getFinger_Left()[0].getBonus(), "  Vitality +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 1 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 2:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Vitality +", self.player.getFinger_Left()[0].getBonus(), "  Dexterity +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 1 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 3:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Vitality +", self.player.getFinger_Left()[0].getBonus(), "  Strength +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 2 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 1:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Dexterity +", self.player.getFinger_Left()[0].getBonus(), "  Vitality +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 3 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 1:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Strength +", self.player.getFinger_Left()[0].getBonus(), "  Vitality +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 2 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 2:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Dexterity +", self.player.getFinger_Left()[0].getBonus(), "  Dexterity +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 3 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 3:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Strength +", self.player.getFinger_Left()[0].getBonus(), "  Strength +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 2 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 3:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Dexterity +", self.player.getFinger_Left()[0].getBonus(), "  Strength +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
            elif self.player.getFinger_Left()[0].getBonus() > 0 and self.player.getFinger_Left()[0].getAttribute() == 3 and self.player.getFinger_Left()[0].getBonus2() > 0 and self.player.getFinger_Left()[0].getAttribute2() == 2:
                print("Finger_Left:   ", self.player.getFinger_Left()[0].getType(), "", " Strength +", self.player.getFinger_Left()[0].getBonus(), "  Dexterity +", self.player.getFinger_Left()[0].getBonus2(), "  Value:", self.player.getFinger_Left()[0].getValue(), "Taler")
        else:
            print("Finger_Left:    empty")
        ####################################################################################################################
        if len(self.player.getFinger_Right()) == 1:
            # Finger_Right 1 Bonus-----------------------------------------------------------------------------------------------------------
            if self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 1 and self.player.getFinger_Right()[0].getBonus2() == 0:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Vitality +", self.player.getFinger_Right()[0].getBonus(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 2 and self.player.getFinger_Right()[0].getBonus2() == 0:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Dexterity +", self.player.getFinger_Right()[0].getBonus(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 3 and self.player.getFinger_Right()[0].getBonus2() == 0:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Strength +", self.player.getFinger_Right()[0].getBonus(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            # Finger_Right 2 Bonus------------------------------------------------------------------------------------------------------------ 
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 1 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 1:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Vitality +", self.player.getFinger_Right()[0].getBonus(), "  Vitality +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 1 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 2:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Vitality +", self.player.getFinger_Right()[0].getBonus(), "  Dexterity +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 1 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 3:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Vitality +", self.player.getFinger_Right()[0].getBonus(), "  Strength +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 2 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 1:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Dexterity +", self.player.getFinger_Right()[0].getBonus(), "  Vitality +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 3 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 1:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Strength +", self.player.getFinger_Right()[0].getBonus(), "  Vitality +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 2 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 2:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Dexterity +", self.player.getFinger_Right()[0].getBonus(), "  Dexterity +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 3 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 3:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Strength +", self.player.getFinger_Right()[0].getBonus(), "  Strength +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 2 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 3:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Dexterity +", self.player.getFinger_Right()[0].getBonus(), "  Strength +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
            elif self.player.getFinger_Right()[0].getBonus() > 0 and self.player.getFinger_Right()[0].getAttribute() == 3 and self.player.getFinger_Right()[0].getBonus2() > 0 and self.player.getFinger_Right()[0].getAttribute2() == 2:
                print("Finger_Right:  ", self.player.getFinger_Right()[0].getType(), "", " Strength +", self.player.getFinger_Right()[0].getBonus(), "  Dexterity +", self.player.getFinger_Right()[0].getBonus2(), "  Value:", self.player.getFinger_Right()[0].getValue(), "Taler")
        else:
            print("Finger_Right:   empty")
        #########################################################################################################################
        if len(self.player.getNeck()) == 1:
            # Neck 1 Bonus-----------------------------------------------------------------------------------------------------------
            if self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 1 and self.player.getNeck()[0].getBonus2() == 0:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Vitality +", self.player.getNeck()[0].getBonus(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 2 and self.player.getNeck()[0].getBonus2() == 0:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Dexterity +", self.player.getNeck()[0].getBonus(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 3 and self.player.getNeck()[0].getBonus2() == 0:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Strength +", self.player.getNeck()[0].getBonus(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            # Neck 2 Bonus------------------------------------------------------------------------------------------------------------ 
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 1 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 1:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Vitality +", self.player.getNeck()[0].getBonus(), "  Vitality +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 1 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 2:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Vitality +", self.player.getNeck()[0].getBonus(), "  Dexterity +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 1 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 3:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Vitality +", self.player.getNeck()[0].getBonus(), "  Strength +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 2 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 1:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Dexterity +", self.player.getNeck()[0].getBonus(), "  Vitality +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 3 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 1:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Strength +", self.player.getNeck()[0].getBonus(), "  Vitality +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 2 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 2:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Dexterity +", self.player.getNeck()[0].getBonus(), "  Dexterity +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            #------------------------------------------------------------
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 3 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 3:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Strength +", self.player.getNeck()[0].getBonus(), "  Strength +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 2 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 3:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Dexterity +", self.player.getNeck()[0].getBonus(), "  Strength +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
            elif self.player.getNeck()[0].getBonus() > 0 and self.player.getNeck()[0].getAttribute() == 3 and self.player.getNeck()[0].getBonus2() > 0 and self.player.getNeck()[0].getAttribute2() == 2:
                print("Neck:          ", self.player.getNeck()[0].getType(), "", " Strength +", self.player.getNeck()[0].getBonus(), "  Dexterity +", self.player.getNeck()[0].getBonus2(), "  Value:", self.player.getNeck()[0].getValue(), "Taler")
        else:
            print("Neck:           empty")
        ###################################################################################################################
        if len(self.player.getHands()[0]) == 1 and len(self.player.getHands()[1]) == 1 and len(self.player.getHands()[2]) == 0 and self.player.getHands()[1][0].getCategory() == "Weapon" and self.player.getThe_Berserker() == True:
            print("")
            print("----------------------------------------------------")
            print(Fore.LIGHTYELLOW_EX + "Weapon: 2x 1-Handweapon, Bonus: + 3% 2nd attack")
            print("----------------------------------------------------")
        elif len(self.player.getHands()[0]) == 1 and len(self.player.getHands()[1]) == 1 and len(self.player.getHands()[2]) == 0 and self.player.getHands()[1][0].getCategory() == "Armor" and self.player.getThe_Defender() == True:
            print("")
            print("----------------------------------------------------")
            print(Fore.LIGHTBLUE_EX + "Weapon: 1x 1-Handweapon + Shield, Bonus:  - 2 armor point needed to get dmg reduction")
            print("----------------------------------------------------")
        elif len(self.player.getHands()[0]) == 0 and len(self.player.getHands()[1]) == 0 and len(self.player.getHands()[2]) == 1 and self.player.getThe_Warrior() == True:
            print("")
            print("----------------------------------------------------")
            print(Fore.LIGHTRED_EX + "Weapon: 1x 2-Handweapon, Bonus: + 7% total damage")
            print("----------------------------------------------------")
        else:
            print("")
            print("----------------------------------------------------")
            print("Weapon:")
            print("----------------------------------------------------")
        if len(self.player.getHands()[0]) == 1 or len(self.player.getHands()[0]) == 0 and len(self.player.getHands()[1]) == 1 or len(self.player.getHands()[1]) == 0 and len(self.player.getHands()[2]) == 0:
            if len(self.player.getHands()[0]) == 1:
                    # Nothing-----------------------------------------------------------------------------
                if self.player.getHands()[0][0].getBonus() == 0:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                # Hands 1 Bonus-------------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 1 and self.player.getHands()[0][0].getBonus2() == 0:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Vitality +", self.player.getHands()[0][0].getBonus(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 2 and self.player.getHands()[0][0].getBonus2() == 0:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[0][0].getBonus(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 3 and self.player.getHands()[0][0].getBonus2() == 0:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Strength +", self.player.getHands()[0][0].getBonus(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                # Hands 2 Bonus-----------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 1 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 1:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Vitality +", self.player.getHands()[0][0].getBonus(), "  Vitality +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 1 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 2:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Vitality +", self.player.getHands()[0][0].getBonus(), "  Dexterity +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 1 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 3:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Vitality +", self.player.getHands()[0][0].getBonus(), "  Strength +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 2 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 1:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[0][0].getBonus(), "  Vitality +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 3 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 1:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Strength +", self.player.getHands()[0][0].getBonus(), "  Vitality +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 2 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 2:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[0][0].getBonus(), "  Dexterity +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 3 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 3:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Strength +", self.player.getHands()[0][0].getBonus(), "  Strength +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 2 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 3:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[0][0].getBonus(), "  Strength +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
                elif self.player.getHands()[0][0].getBonus() > 0 and self.player.getHands()[0][0].getAttribute() == 3 and self.player.getHands()[0][0].getBonus2() > 0 and self.player.getHands()[0][0].getAttribute2() == 2:
                    print("Right_Hand:    ", self.player.getHands()[0][0].getType(), self.player.getHands()[0][0].getHands(), "", "Dmg:", self.player.getHands()[0][0].getMinDmg(), "-", self.player.getHands()[0][0].getMaxDmg(), "  Strength +", self.player.getHands()[0][0].getBonus(), "  Dexterity +", self.player.getHands()[0][0].getBonus2(), "  Value:", self.player.getHands()[0][0].getValue(), "Taler")
            elif len(self.player.getHands()[0]) == 0:
                print("Right_Hand:    empty")
            ###################################################################################################################
            if len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getCategory() == "Weapon":
                    # Nothing-----------------------------------------------------------------------------
                if self.player.getHands()[1][0].getBonus() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                # Hands 1 Bonus-------------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Strength +", self.player.getHands()[1][0].getBonus(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                # Hands 2 Bonus-----------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 1:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Vitality +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 2:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Dexterity +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 3:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Strength +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 1:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Vitality +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 1:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Strength +", self.player.getHands()[1][0].getBonus(), "  Vitality +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 2:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Dexterity +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 3:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Strength +", self.player.getHands()[1][0].getBonus(), "  Strength +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 3:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Strength +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 2:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getType(), self.player.getHands()[1][0].getHands(), "", "Dmg:", self.player.getHands()[1][0].getMinDmg(), "-", self.player.getHands()[1][0].getMaxDmg(), "  Strength +", self.player.getHands()[1][0].getBonus(), "  Dexterity +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
            elif len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getCategory() == "Armor":
                    # Nothing-----------------------------------------------------------------------------
                if self.player.getHands()[1][0].getBonus() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                # Hands 1 Bonus-------------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() == 0:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Strength +", self.player.getHands()[1][0].getBonus(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                # Hands 2 Bonus-----------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 1:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Vitality +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 2:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Dexterity +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 1 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 3:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Vitality +", self.player.getHands()[1][0].getBonus(), "  Strength +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 1:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Vitality +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 1:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Strength +", self.player.getHands()[1][0].getBonus(), "  Vitality +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 2:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Dexterity +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 3:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Strength +", self.player.getHands()[1][0].getBonus(), "  Strength +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 2 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 3:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Dexterity +", self.player.getHands()[1][0].getBonus(), "  Strength +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
                elif self.player.getHands()[1][0].getBonus() > 0 and self.player.getHands()[1][0].getAttribute() == 3 and self.player.getHands()[1][0].getBonus2() > 0 and self.player.getHands()[1][0].getAttribute2() == 2:
                    print("Left_Hand:     ", self.player.getHands()[1][0].getName(), "", "Armor:", self.player.getHands()[1][0].getArmor(), "", "Blockchance:", self.player.getHands()[1][0].getBlockchance(), "%", "  Strength +", self.player.getHands()[1][0].getBonus(), "  Dexterity +", self.player.getHands()[1][0].getBonus2(), "  Value:", self.player.getHands()[1][0].getValue(), "Taler")
            elif len(self.player.getHands()[1]) == 0:
                print("Left_Hand:     empty")
        elif len(self.player.getHands()[0]) == 0 and len(self.player.getHands()[1]) == 0 and len(self.player.getHands()[2]) == 1:
            if len(self.player.getHands()[2]) == 1:
                # Nothing-----------------------------------------------------------------------------
                if self.player.getHands()[2][0].getBonus() == 0:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                # Hands 1 Bonus-------------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 1 and self.player.getHands()[2][0].getBonus2() == 0:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Vitality +", self.player.getHands()[2][0].getBonus(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 2 and self.player.getHands()[2][0].getBonus2() == 0:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[2][0].getBonus(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 3 and self.player.getHands()[2][0].getBonus2() == 0:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Strength +", self.player.getHands()[2][0].getBonus(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                # Hands 2 Bonus-----------------------------------------------------------------------------------------------------------
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 1 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 1:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Vitality +", self.player.getHands()[2][0].getBonus(), "  Vitality +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 1 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 2:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Vitality +", self.player.getHands()[2][0].getBonus(), "  Dexterity +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 1 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 3:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Vitality +", self.player.getHands()[2][0].getBonus(), "  Strength +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 2 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 1:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[2][0].getBonus(), "  Vitality +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 3 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 1:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Strength +", self.player.getHands()[2][0].getBonus(), "  Vitality +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 2 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 2:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[2][0].getBonus(), "  Dexterity +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                #----------------------------------------------------------------------
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 3 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 3:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Strength +", self.player.getHands()[2][0].getBonus(), "  Strength +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 2 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 3:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Dexterity +", self.player.getHands()[2][0].getBonus(), "  Strength +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                elif self.player.getHands()[2][0].getBonus() > 0 and self.player.getHands()[2][0].getAttribute() == 3 and self.player.getHands()[2][0].getBonus2() > 0 and self.player.getHands()[2][0].getAttribute2() == 2:
                    print("Both_Hands:    ", self.player.getHands()[2][0].getType(), self.player.getHands()[2][0].getHands(), "", "Dmg:", self.player.getHands()[2][0].getMinDmg(), "-", self.player.getHands()[2][0].getMaxDmg(), "  Strength +", self.player.getHands()[2][0].getBonus(), "  Dexterity +", self.player.getHands()[2][0].getBonus2(), "  Value:", self.player.getHands()[2][0].getValue(), "Taler")
                #####################################################################################################################################
        print("")
        print("----------------------------------------------------")
        print("Character Info:")
        print("----------------------------------------------------")
        if self.player.getGender() == "w":
            print("Name:", self.player.getName(), "  Gender: Female", "  Race:", self.player.getRace())
        else:
            print("Name:", self.player.getName(), "  Gender: Male", "  Race:", self.player.getRace())
        print("----------------------------------------------------")
        print("Life points:   ", self.player.getHealth(),"/",self.player.getMaxHealth())
        print("Focus points:  ", self.player.getFocus_points(),"/",self.player.getMaxFocus_points())
        print("Strength:      ", self.player.getStrength(), "      [ 1 Strength = +1 total damage ]          Counterattack Chance:", self.player.getCounterattack())
        print("Dexterity:     ", self.player.getDexterity(), "      [ 1 Dexterity = +1% chance 2nd attack ]      Dexterity Chance:", self.player.getEvasion())
        print("Vitality:      ", self.player.getVitality(), "      [ 1 Vitality = +10 max. health ]")
        print("----------------------------------------------------")
        print("Chance to escape:  ", self.player.getEscape(),"/ 6")
        print("Blockchance:       ", self.player.getBlockchance(),"%")
        print("Chance 2nd Attack: ", self.player.getAttack2(),"%")
        print("Total Armor:       ", self.player.getArmor())
        print("Damage Reduction:  ", self.player.getReduction(self.player.getReductionBonus()), "  [Every", self.player.getReductionBonus(), "Armor, 1 dmg will be absorbed.]")
        # Min-Max Damage 2x 1Hand
        if len(self.player.getHands()[0]) == 1 and len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getCategory() == "Weapon" and len(self.player.getHands()[2]) == 0:
            print("Total Damage:      ", (self.player.getHands()[0][0].getMinDmg() + self.player.getHands()[1][0].getMinDmg() + self.player.getStrength()),"-", self.player.getHands()[0][0].getMaxDmg() + self.player.getHands()[1][0].getMaxDmg() + self.player.getStrength())
        # Min-Max Damage right Hand
        elif len(self.player.getHands()[0]) == 1 and (len(self.player.getHands()[1]) == 0 or (len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getCategory() == "Armor")) and len(self.player.getHands()[2]) == 0:
            print("Total Damage:      ", (self.player.getHands()[0][0].getMinDmg() + self.player.getStrength()),"-", self.player.getHands()[0][0].getMaxDmg() + self.player.getStrength())
        # Min-Max Damage left Hand
        elif len(self.player.getHands()[0]) == 0 and len(self.player.getHands()[1]) == 1 and self.player.getHands()[1][0].getCategory() == "Weapon" and len(self.player.getHands()[2]) == 0:
            print("Total Damage:      ", (self.player.getHands()[1][0].getMinDmg() + self.player.getStrength()),"-", self.player.getHands()[1][0].getMaxDmg() + self.player.getStrength())
        # Min-Max Damage 1x 2Hand
        elif len(self.player.getHands()[0]) == 0 and len(self.player.getHands()[1]) == 0 and len(self.player.getHands()[2]) == 1:
            print("Total Damage:      ", (self.player.getHands()[2][0].getMinDmg() + self.player.getStrength()) + strength_bonus,"-", self.player.getHands()[2][0].getMaxDmg() + self.player.getStrength() + strength_bonus)
        # no Weapon
        else:
            print("Total Damage:      ", (self.player.getStrength()),"-", self.player.getStrength())
        print("----------------------------------------------------")
        print("Skill points:       ", self.player.getSkill_points())
        print("LVL:                ", self.player.getLVL())
        print("Experience:         ", len(self.player.Xp),"/",math.ceil(self.player.lvl_counter))
        print("Max.Inventory Size: ", self.player.Max_Length)
        print("Taler:              ", self.player.getTaler())
        print("Location:", maps.Celtic_Continent.getName(), "  Coordinates: Y:", self.player.y,", X:", self.player.x)
        
        
        
