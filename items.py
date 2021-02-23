import random
from colorama import init, Fore, Back, Style
init(wrap=False)
init(autoreset=True)

class Weapon():
    def __init__(self, area, category, value, hands, dmg, mindmg, maxdmg, type, bonus, attribute, bonus2, attribute2):
        self.Area = area
        self.Category = category
        self.Value = value
        self.Hands = hands
        self.Dmg = dmg
        self.Type = type
        self.Bonus = bonus
        self.Attribute = attribute
        self.Bonus2 = bonus2
        self.Attribute2 = attribute2
        self.MinDmg = mindmg
        self.MaxDmg = maxdmg
    def getArea(self):
        return self.Area
    def getCategory(self):
        return self.Category
    def getValue(self):
        self.Value = ((self.getMinDmg() + self.getMaxDmg()) + (self.Bonus * 40) + (self.Bonus2 * 40))
        return self.Value
    def getHands(self):
        return self.Hands
    def getMinDmg(self):
        return self.MinDmg
    def getMaxDmg(self):
        return self.MaxDmg
    def getDmg(self):
        zufall = random.randint(self.MinDmg, self.MaxDmg)
        self.Dmg = zufall
        return self.Dmg
    def getType(self):
        return self.Type
    def getBonus(self):
        return self.Bonus
    def getAttribute(self):
        return self.Attribute
    def getBonus2(self):
        return self.Bonus2
    def getAttribute2(self):
        return self.Attribute2

class Armor():
    def __init__(self, area, category, value, type, material, armor, noshield, bonus, attribute, bonus2, attribute2):
        self.Area = area
        self.Category = category
        self.Value = value
        self.Type = type
        self.Material = material
        self.Armor = armor
        self.NoShield = noshield
        self.Bonus = bonus
        self.Attribute = attribute
        self.Bonus2 = bonus2
        self.Attribute2 = attribute2
    def getArea(self):
        return self.Area
    def getCategory(self):
        return self.Category
    def getValue(self):
        self.Value = self.Armor + (self.Bonus * 40) + (self.Bonus2 * 40)
        return self.Value
    def getArmor(self):
        return self.Armor
    def getType(self):
        return self.Type
    def getMaterial(self):
        return self.Material
    def getNoShield(self):
        return self.NoShield
    def getBonus(self):
        return self.Bonus
    def getAttribute(self):
        return self.Attribute
    def getBonus2(self):
        return self.Bonus2
    def getAttribute2(self):
        return self.Attribute2

class Shield():
    def __init__(self, area, category, value, type, armor, blockchance, bonus, attribute, bonus2, attribute2, name):
        self.Area = area
        self.Category = category
        self.Value = value
        self.Type = type
        self.Armor = armor
        self.Blockchance = blockchance
        self.Bonus = bonus
        self.Attribute = attribute
        self.Bonus2 = bonus2
        self.Attribute2 = attribute2
        self.Name = name
    def getArea(self):
        return self.Area
    def getCategory(self):
        return self.Category
    def getValue(self):
        self.Value = self.Armor + (self.Bonus * 40) + (self.Bonus2 * 40) + (self.Blockchance * 2)
        return self.Value
    def getType(self):
        return self.Type
    def getArmor(self):
        return self.Armor
    def getBlockchance(self):
        return self.Blockchance
    def getBonus(self):
        return self.Bonus
    def getAttribute(self):
        return self.Attribute
    def getBonus2(self):
        return self.Bonus2
    def getAttribute2(self):
        return self.Attribute2
    def getName(self):
        return self.Name


class Jewellery():
    def __init__(self, area, category, value, type, bonus, attribute, bonus2, attribute2):
        self.Area = area
        self.Category = category
        self.Value = value
        self.Type = type
        self.Bonus = bonus
        self.Attribute = attribute
        self.Bonus2 = bonus2
        self.Attribute2 = attribute2
    def getArea(self):
        return self.Area
    def getCategory(self):
        return self.Category
    def getValue(self):
        self.Value = (self.Bonus * 80) + (self.Bonus2 * 80)
        return self.Value
    def getType(self):
        return self.Type
    def getBonus(self):
        return self.Bonus
    def getAttribute(self):
        return self.Attribute
    def getBonus2(self):
        return self.Bonus2
    def getAttribute2(self):
        return self.Attribute2

class Potion():
    def __init__(self, category, name, size, value):
        self.Name = name
        self.Size = size
        self.Value = value
        self.Category = category
        self.Stack_Size = 9
        self.Stack = []
    def getCategory(self):
        return self.Category
    def getName(self):
        return self.Name
    def setName(self, new_Name):
        self.Name = new_Name
    def getSize(self, race):
        a = self.Size
        if race == "Kro'L":
            a = a * 1.10
            return round(a)
        else:
            return a
    def setSize(self, new_Size):
        self.Size = new_Size
    def getValue(self):
        self.Value = (self.Size * 1)
        return self.Value
    def getStack(self):
        return self.Stack
    def setStack(self, new_Stack):
        self.Stack = new_Stack



##########################################################---- Potions ----####################################################################
Basic_Potion = Potion("Potion", "Small_Potion", 15, 0)
Normal_Potion = Potion("Potion", "Normal_Potion", 35, 0)
Big_Potion = Potion("Potion", "Big_Potion", 80, 0)     
###########################################################---- Weapons ----####################################################################
# Basic 1-Hand Weapons
Basic_Dagger_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 1, 7, "Dagger", 0, random.randint(1,3), 0, random.randint(1,3))
Basic_Axe_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 2, 6, "Axe", 0, random.randint(1,3), 0, random.randint(1,3))
Basic_Sword_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 3, 5, "Sword", 0, random.randint(1,3), 0, random.randint(1,3))
Basic_Hammer_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 4, 4, "Hammer", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic 2-Hand Weapons
Basic_Spear_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 1, 19, "Spear", 0, random.randint(1,3), 0, random.randint(1,3))
Basic_Axe_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 6, 15, "Axe", 0, random.randint(1,3), 0, random.randint(1,3))
Basic_Sword_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 9, 12, "Sword", 0, random.randint(1,3), 0, random.randint(1,3))
Basic_Hammer_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 10, 11, "Hammer", 0, random.randint(1,3), 0, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------
# Unusual 1-Hand Weapons
Unusual_Dagger_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 1, 13, Fore.GREEN+"Dagger", 1, random.randint(1,3), 0, random.randint(1,3))
Unusual_Axe_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 4, 9, Fore.GREEN+"Axe", 1, random.randint(1,3), 0, random.randint(1,3))
Unusual_Sword_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 5, 8, Fore.GREEN+"Sword", 1, random.randint(1,3), 0, random.randint(1,3))
Unusual_Hammer_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 6, 7, Fore.GREEN+"Hammer", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual 2-Hand Weapons
Unusual_Spear_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 1, 24, Fore.GREEN+"Spear", 1, random.randint(1,3), 0, random.randint(1,3))
Unusual_Axe_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 9, 18, Fore.GREEN+"Axe", 1, random.randint(1,3), 0, random.randint(1,3))
Unusual_Sword_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 12, 15, Fore.GREEN+"Sword", 1, random.randint(1,3), 0, random.randint(1,3))
Unusual_Hammer_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 13, 14, Fore.GREEN+"Hammer", 1, random.randint(1,3), 0, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------
# Rare 1-Hand Weapons
Rare_Dagger_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 1, 18, Fore.BLUE+"Dagger", 1, random.randint(1,3), 1, random.randint(1,3))
Rare_Axe_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 6, 12, Fore.BLUE+"Axe", 1, random.randint(1,3), 1, random.randint(1,3))
Rare_Sword_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 7, 10, Fore.BLUE+"Sword", 1, random.randint(1,3), 1, random.randint(1,3))
Rare_Hammer_1Hand = Weapon( "Hands", "Weapon", 0, "1-Hand", 0, 8, 9, Fore.BLUE+"Hammer", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare 2-Hand Weapons
Rare_Spear_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 1, 30, Fore.BLUE+"Spear", 1, random.randint(1,3), 1, random.randint(1,3))
Rare_Axe_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 12, 21, Fore.BLUE+"Axe", 1, random.randint(1,3), 1, random.randint(1,3))
Rare_Sword_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 15, 18, Fore.BLUE+"Sword", 1, random.randint(1,3), 1, random.randint(1,3))
Rare_Hammer_2Hand = Weapon( "Hands", "Weapon", 0, "2-Hand", 0, 16, 17, Fore.BLUE+"Hammer", 1, random.randint(1,3), 1, random.randint(1,3))

###########################################################---- Armor ----####################################################################
# Basic Headgear _Leather
Basic_Head_Leather = Armor("Head", "Armor", 0, "Leather_Head", "Leather", random.randint(1,1), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Body Leather
Basic_Body_Leather = Armor("Body", "Armor", 0, "Leather_Body", "Leather", random.randint(2,4), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Legs Leather
Basic_Legs_Leather = Armor("Legs", "Armor", 0, "Leather_Legs", "Leather", random.randint(1,2), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Feet Leather
Basic_Feet_Leather = Armor("Feet", "Armor", 0, "Leather_Feet", "Leather", random.randint(1,1), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------------------
# Basic Headgear _Chain
Basic_Head_Chain = Armor("Head", "Armor", 0, "Chain_Head", "Chain", random.randint(1,2), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Body Chain
Basic_Body_Chain = Armor("Body", "Armor", 0, "Chain_Body", "Chain", random.randint(4,6), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Legs Chain
Basic_Legs_Chain = Armor("Legs", "Armor", 0, "Chain_Legs", "Chain", random.randint(2,3), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Feet Chain
Basic_Feet_Chain = Armor("Feet", "Armor", 0, "Chain_Feet", "Chain", random.randint(1,2), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------------------
# Basic Headgear _Plate
Basic_Head_Plate = Armor("Head", "Armor", 0, "Plate_Head", "Plate", random.randint(2,3), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Body Plate
Basic_Body_Plate = Armor("Body", "Armor", 0, "Plate_Body", "Plate", random.randint(7,9), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Legs Plate
Basic_Legs_Plate = Armor("Legs", "Armor", 0, "Plate_Legs", "Plate", random.randint(4,5), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
# Basic Feet Plate
Basic_Feet_Plate = Armor("Feet", "Armor", 0, "Plate_Feet", "Plate", random.randint(2,3), "NoShield", 0, random.randint(1,3), 0, random.randint(1,3))
###############################################################################################################################
# Unusual Headgear Leather
Unusual_Head_Leather = Armor("Head", "Armor", 0, Fore.GREEN+"Leather_Head", "Leather", random.randint(1,2), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Body Leather
Unusual_Body_Leather = Armor("Body", "Armor", 0, Fore.GREEN+"Leather_Body", "Leather", random.randint(4,6), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Legs Leather
Unusual_Legs_Leather = Armor("Legs", "Armor", 0, Fore.GREEN+"Leather_Legs", "Leather", random.randint(2,5), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Feet Leather
Unusual_Feet_Leather = Armor("Feet", "Armor", 0, Fore.GREEN+"Leather_Feet", "Leather", random.randint(1,2), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------------------
# Unusual Headgear Chain
Unusual_Head_Chain = Armor("Head", "Armor", 0, Fore.GREEN+"Chain_Head", "Chain", random.randint(2,3), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Body Chain
Unusual_Body_Chain = Armor("Body", "Armor", 0, Fore.GREEN+"Chain_Body", "Chain", random.randint(6,8), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Legs Chain
Unusual_Legs_Chain = Armor("Legs", "Armor", 0, Fore.GREEN+"Chain_Legs", "Chain", random.randint(3,6), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Feet Chain
Unusual_Feet_Chain = Armor("Feet", "Armor", 0, Fore.GREEN+"Chain_Feet", "Chain", random.randint(2,3), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------------------
# Unusual Headgear Plate
Unusual_Head_Plate = Armor("Head", "Armor", 0, Fore.GREEN+"Plate_Head", "Plate", random.randint(3,5), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Body Plate
Unusual_Body_Plate = Armor("Body", "Armor", 0, Fore.GREEN+"Plate_Body", "Plate", random.randint(9,12), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Legs Plate
Unusual_Legs_Plate = Armor("Legs", "Armor", 0, Fore.GREEN+"Plate_Legs", "Plate", random.randint(5,8), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
# Unusual Feet Plate
Unusual_Feet_Plate = Armor("Feet", "Armor", 0, Fore.GREEN+"Plate_Feet", "Plate", random.randint(3,5), "NoShield", 1, random.randint(1,3), 0, random.randint(1,3))
###############################################################################################################################
# Rare Headgear Leather
Rare_Head_Leather = Armor("Head", "Armor", 0, Fore.BLUE+"Leather_Head", "Leather", random.randint(2,4), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Body Leather
Rare_Body_Leather = Armor("Body", "Armor", 0, Fore.BLUE+"Leather_Body", "Leather", random.randint(6,9), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Legs Leather
Rare_Legs_Leather = Armor("Legs", "Armor", 0, Fore.BLUE+"Leather_Legs", "Leather", random.randint(4,8), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Feet Leather
Rare_Feet_Leather = Armor("Feet", "Armor", 0, Fore.BLUE+"Leather_Feet", "Leather", random.randint(2,4), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------------------
# Rare Headgear Chain
Rare_Head_Chain = Armor("Head", "Armor", 0, Fore.BLUE+"Chain_Head", "Chain", random.randint(3,5), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Body Chain
Rare_Body_Chain = Armor("Body", "Armor", 0, Fore.BLUE+"Chain_Body", "Chain", random.randint(9,12), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Legs Chain
Rare_Legs_Chain = Armor("Legs", "Armor", 0, Fore.BLUE+"Chain_Legs", "Chain", random.randint(6,10), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Feet Chain
Rare_Feet_Chain = Armor("Feet", "Armor", 0, Fore.BLUE+"Chain_Feet", "Chain", random.randint(3,5), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
#------------------------------------------------------------------------------------------------------------------------------
# Rare Headgear Plate
Rare_Head_Plate = Armor("Head", "Armor", 0, Fore.BLUE+"Plate_Head", "Plate", random.randint(5,7), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Body Plate
Rare_Body_Plate = Armor("Body", "Armor", 0, Fore.BLUE+"Plate_Body", "Plate", random.randint(12,16), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Legs Plate
Rare_Legs_Plate = Armor("Legs", "Armor", 0, Fore.BLUE+"Plate_Legs", "Plate", random.randint(8,12), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Feet Plate
Rare_Feet_Plate = Armor("Feet", "Armor", 0, Fore.BLUE+"Plate_Feet", "Plate", random.randint(5,7), "NoShield", 1, random.randint(1,3), 1, random.randint(1,3))

###########################################################---- Shield ----####################################################################
# Basic Shield
Basic_Shield = Shield("1-Hand", "Armor", 0, "Shield", random.randint(3,6), random.randint(3,5), 0, random.randint(1,3), 0, random.randint(1,3), "Shield")
# Unusual Shield
Unusual_Shield = Shield("1-Hand", "Armor", 0, "Shield", random.randint(6,11), random.randint(4,6), 1, random.randint(1,3), 0, random.randint(1,3), Fore.GREEN + "Shield")
# Rare Shield
Rare_Shield = Shield("1-Hand", "Armor", 0, "Shield", random.randint(11,16), random.randint(6,8), 1, random.randint(1,3), 1, random.randint(1,3), Fore.BLUE + "Shield")

########################################################## ---- Earring ---- ####################################################################
# area, category, value, type, bonus, attribute
# Unusual Earring
Unusual_Earring = Jewellery("Earring", "Jewellery", 0, Fore.GREEN+"Earring", 1, random.randint(1,3), 0, random.randint(1,3))
# Rare Earring
Rare_Earring = Jewellery("Earring", "Jewellery", 0, Fore.BLUE+"Earring", 1, random.randint(1,3), 1, random.randint(1,3))

################################################################# ---- Ring ---- ##############################################################
# Unusual Ring
Unusual_Ring = Jewellery("Ring", "Jewellery", 0, Fore.GREEN+"Ring", 1, random.randint(1,3), 0, random.randint(1,3))
# Rare Ring
Rare_Ring = Jewellery("Ring", "Jewellery", 0, Fore.BLUE+"Ring", 1, random.randint(1,3), 1, random.randint(1,3))

################################################################# ---- Amulet ---- ##############################################################
# Unusual Amulet
Unusual_Amulet = Jewellery("Amulet", "Jewellery", 0, Fore.GREEN+"Amulet", 1, random.randint(1,3), 1, random.randint(1,3))
# Rare Amulet
Rare_Amulet = Jewellery("Amulet", "Jewellery", 0, Fore.BLUE+"Amulet", 2, random.randint(1,3), 1, random.randint(1,3))

basic_item_list = [Basic_Sword_1Hand, Basic_Spear_2Hand, Basic_Potion, Basic_Body_Chain, Basic_Axe_2Hand, Basic_Head_Leather,
Basic_Hammer_2Hand, Basic_Head_Chain, Basic_Hammer_1Hand, Basic_Head_Plate, Basic_Shield, Basic_Body_Leather, Basic_Body_Plate,
Basic_Sword_2Hand, Basic_Legs_Leather, Basic_Potion, Basic_Axe_1Hand, Basic_Feet_Chain, Basic_Legs_Chain, Basic_Legs_Plate, Basic_Dagger_1Hand, Basic_Feet_Leather, Basic_Feet_Plate]

unusual_item_list = [Unusual_Sword_1Hand, Normal_Potion, Unusual_Spear_2Hand, Unusual_Earring, Unusual_Body_Chain, Unusual_Axe_2Hand, Unusual_Head_Leather,
Unusual_Hammer_2Hand, Basic_Potion, Unusual_Amulet, Unusual_Head_Chain, Unusual_Hammer_1Hand, Unusual_Head_Plate, Unusual_Shield, Unusual_Body_Plate,
Unusual_Sword_2Hand, Unusual_Legs_Leather, Unusual_Axe_1Hand, Unusual_Feet_Chain, Normal_Potion, Unusual_Legs_Chain, Unusual_Dagger_1Hand, Unusual_Feet_Leather,
Unusual_Feet_Plate, Unusual_Legs_Plate, Unusual_Body_Leather, Unusual_Ring]
