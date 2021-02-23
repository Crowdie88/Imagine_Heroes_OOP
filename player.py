import sys
# import only system from os 
from os import system, name, execl
# import sleep to show output for some time period 
from time import sleep
# color und styles
from colorama import init, Fore, Back, Style
init(wrap=False)
init(autoreset=True)
# Random
import random
# math
import math
# sound
import winsound
#skill tree
import skill_tree

def clear():
        _ = system('cls')

class Player():

    def __init__(self, name, gender, race):
        self.__Name = name
        self.x = 500
        self.y = -250
        self.__velocity = 1
        self.__Gender = gender
        self.__Race = race
        self.__Strength = 0
        self.__Dexterity = 0
        self.__Vitality = 5
        self.Head = []
        self.Ear_left = []
        self.Ear_right = []
        self.Neck = []
        self.Body = []
        self.Hands = [[], [], []]
        self.Finger_left = []
        self.Finger_right = []
        self.Legs = []
        self.Feet = []
        self.__MaxHealth = 0
        self.Dmg = 0
        self.Xp = []
        self.Lvl = 1
        self.Armor = 0
        self.Inventory = []
        self.Reduction = 0
        self.Max_Length = 10
        self.lvl_counter = 10
        self.lvl_difficult = 1.5
        self.quest_log = []
        self.Taler = 0
        self.Escape = 0
        self.Reduction_bonus = 10
        self.MaxFocus_points = 5
        self.Focus_points = self.MaxFocus_points
        self.Skill_points = 0
        #----------------------------------------------------- Skill
        # counter
        self.Armory_counter = 1
        self.Passive_counter = 1
        # Armory ----
        self.The_Warrior = False
        self.The_Berserker = False
        self.The_Defender = False
        # Passive
        self.Evasion = 0
        self.Evasion_switch = False
        self.Counterattack = 0
        self.Counterattack_switch = False
        self.Push_Back_switch = False
        # Push_Back = getBlocken
        # ---------------------------- Race Bonus
        # Human + 5% Blockchance
        if self.__Race == "Human":
            self.Blockchance = 5
        else:
            self.Blockchance = 0
        # ---------------------------------------
        # Nefler + 3% Attack2
        if self.__Race == "Nefler":
            self.Attack2 = 3
        else:
            self.Attack2 = 0
        # ---------------------------------------
        # Bonus Kro'L in function getMaxHealth
        if self.__Race == "Kro'L":
            self.__MaxHealth = round((self.__Vitality * 10) * 1.10)
        else:
            self.__MaxHealth = self.__Vitality * 10
        self.__Health = self.__MaxHealth
    #---------------------------------------------------------- Gender
    def getGender(self):
        return self.__Gender
    #---------------------------------------------------------- Gender
    def getRace(self):
        return self.__Race
    #---------------------------------------------------------- Taler
    def getTaler(self):
        return self.Taler
    def setTaler(self, new_Taler):
        self.Taler = new_Taler
    # --------------------------------------------------------- quest_log
    def getQlog(self):
        if len(self.quest_log) > 0:
            for i in self.quest_log:
                print(Fore.YELLOW + i)
                print("")
        else:
            print("")
            print("Your Questlog is empty...")
    # --------------------------------------------------------- Name
    def getName(self):
        return self.__Name
    def setName(self, new_Name):
        self.__Name = new_Name
    #------------------------------------------------------- Skill
    #--------------------------------------------------
    def getArmory_counter(self):
        return self.Armory_counter
    def setArmory_counter(self, new_Armory_counter):
        self.Armory_counter = new_Armory_counter
    #--------------------------------------------------
    def getPassive_counter(self):
        return self.Passive_counter
    def setPassive_counter(self, new_Passic_counter):
        self.Passive_counter = new_Passic_counter
    # Armory ----
    def getThe_Warrior(self):
        return self.The_Warrior
    def setThe_Warrior(self, new_The_Warrior):
        self.The_Warrior = new_The_Warrior
    #-----------------------------------
    def getThe_Berserker(self):
        return self.The_Berserker
    def setThe_Berserker(self, new_The_Berserker):
        self.The_Berserker = new_The_Berserker
    #-----------------------------------
    def getThe_Defender(self):
        return self.The_Defender
    def setThe_Defender(self, new_The_Defender):
        self.The_Defender = new_The_Defender
    # Passive ----
    def getEvasion(self):
        if self.Evasion_switch == True:
            self.setEvasion(round(self.getDexterity() * 0.25))
        return self.Evasion
    def setEvasion(self, new_Evasion):
        self.Evasion = new_Evasion
    def getEvasion_Switch(self):
        return self.Evasion_switch
    def setEvasion_Switch(self, new_Evasion_Switch):
        self.Evasion_switch = new_Evasion_Switch
    # ----
    def getCounterattack(self):
        if self.Counterattack_switch == True:
            self.setCounterattack(round(self.getStrength() * 0.2))
        return self.Counterattack
    def setCounterattack(self, new_Counterattack):
        self.Counterattack = new_Counterattack
    def getCounterattack_Switch(self):
        return self.Counterattack_switch
    def setCounterattack_Switch(self, new_Counterattack_Switch):
        self.Counterattack_switch = new_Counterattack_Switch
    # ----
    def getPush_Back_Switch(self):
        return self.Push_Back_switch
    def setPush_Back_Switch(self, new_Push_Back_Switch):
        self.Push_Back_switch = new_Push_Back_Switch
    # --------------------------------------------------------- Focus Points
    def getFocus_points(self):
        return self.Focus_points
    def setFocus_points(self, new_Focus_points):
        self.Focus_points = new_Focus_points

    def getMaxFocus_points(self):
        return self.MaxFocus_points
    def setMaxFocus_points(self, new_MaxFocus_points):
        self.MaxFocus_points = new_MaxFocus_points
    # --------------------------------------------------------- Skill points
    def getSkill_points(self):
        return self.Skill_points
    def setSkill_points(self, new_Skill_points):
        self.Skill_points = new_Skill_points
    #---------------------------------------------------------- limit for the inventory
    def push(self, st):
        info = False
        if len(self.Inventory) == self.Max_Length:
            for i in self.Inventory:
                if st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Small_Potion" and i.getName() == "Small_Potion" and len(i.getStack()) < i.Stack_Size:
                    i.getStack().append(st)
                    info = True
                    break
                elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Small_Potion" and i.getName() == "Small_Potion" and len(i.getStack()) >= i.Stack_Size:
                    self.Inventory.append(st)
                    del self.Inventory[10]
                    print("Inventory is full...")
                    info = True
                    break
                elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Normal_Potion" and i.getName() == "Normal_Potion" and len(i.getStack()) < i.Stack_Size:
                    i.getStack().append(st)
                    info = True
                    break
                elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Normal_Potion" and i.getName() == "Normal_Potion" and len(i.getStack()) >= i.Stack_Size:
                    self.Inventory.append(st)
                    del self.Inventory[10]
                    print("Inventory is full...")
                    info = True
                    break
                elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Big_Potion" and i.getName() == "Big_Potion" and len(i.getStack()) < i.Stack_Size:
                    i.getStack().append(st)
                    info = True
                    break
                elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Big_Potion" and i.getName() == "Big_Potion" and len(i.getStack()) >= i.Stack_Size:
                    self.Inventory.append(st)
                    del self.Inventory[10]
                    print("Inventory is full...")
                    info = True
                    break
            if info == False:
                self.Inventory.append(st)
                del self.Inventory[10]
                print("Inventory is full...")
        elif len(self.Inventory) < self.Max_Length:
            if len(self.Inventory) == 0:
                self.Inventory.append(st)
            else:
                for i in self.Inventory:
                    if st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Small_Potion" and i.getName() == "Small_Potion" and len(i.getStack()) < i.Stack_Size:
                        i.getStack().append(st)
                        info = True
                        break
                    elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Small_Potion" and i.getName() == "Small_Potion" and len(i.getStack()) >= i.Stack_Size:
                        self.Inventory.append(st)
                        del self.Inventory[10]
                        print("Inventory is full...")
                        info = True
                        break
                    elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Normal_Potion" and i.getName() == "Normal_Potion" and len(i.getStack()) < i.Stack_Size:
                        i.getStack().append(st)
                        info = True
                        break
                    elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Normal_Potion" and i.getName() == "Normal_Potion" and len(i.getStack()) >= i.Stack_Size:
                        self.Inventory.append(st)
                        del self.Inventory[10]
                        print("Inventory is full...")
                        info = True
                        break
                    elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Big_Potion" and i.getName() == "Big_Potion" and len(i.getStack()) < i.Stack_Size:
                        i.getStack().append(st)
                        info = True
                        break
                    elif st.getCategory() == "Potion" and i.getCategory() == "Potion" and st.getName() == "Big_Potion" and i.getName() == "Big_Potion" and len(i.getStack()) >= i.Stack_Size:
                        self.Inventory.append(st)
                        del self.Inventory[10]
                        print("Inventory is full...")
                        info = True
                        break
                if info == False:
                    self.Inventory.append(st)
    #---------------------------------------------------------- Position self.x
    def getX(self):
        return self.x
    def setX(self, new_X):
        self.x = new_X
    #---------------------------------------------------------- Position self.y
    def getY(self):
        return self.y
    def setY(self, new_Y):
        self.y = new_Y
    # --------------------------------------------------------- Move
    def move(self, walk):
        if walk == "d":
            self.x += self.__velocity
        elif walk == "a":
            self.x -= self.__velocity
        elif walk == "w":
            self.y += self.__velocity
        elif walk == "s":
            self.y -= self.__velocity
    #---------------------------------------------------------- Escape
    def getEscape(self):
        a = self.Escape
        if len(self.getFeet()) == 1 and self.getFeet()[0].getMaterial() == "Leather":
            a += 3
        elif len(self.getFeet()) == 1 and self.getFeet()[0].getMaterial() == "Chain":
            a += 2
        elif len(self.getFeet()) == 1 and self.getFeet()[0].getMaterial() == "Plate":
            a += 1
        else:
            a += 0
        return a
    def setEscape(self, new_Escape):
        self.Escape = new_Escape
    #---------------------------------------------------------- Attack2
    def getAttack2(self):
        a = self.Attack2 + self.getDexterity()
        return a
    def setAttack2(self, new_Attack2):
        self.Attack2 = new_Attack2
    #---------------------------------------------------------- XP
    def getXP(self):
        if len(self.Xp) >= self.lvl_counter:
            self.lvl_counter = self.lvl_counter * self.lvl_difficult
            self.Lvl += 1
            winsound.PlaySound("sounds\\lvlup_donner.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            print("")
            print(Fore.LIGHTMAGENTA_EX + "LVL UP! Your current lvl is", self.Lvl)
            print("")
            print(Fore.LIGHTMAGENTA_EX + "You can increase one of your attributes")
            print("")
            print(Fore.LIGHTRED_EX + "( 1 ) Increase your strength by 1")
            print(Fore.LIGHTRED_EX + "      Currently you have a basic strength of:", self.__Strength)
            print("")
            print(Fore.LIGHTYELLOW_EX + "( 2 ) Increase your dexterity by 1")
            print(Fore.LIGHTYELLOW_EX + "      Currently you have a basic dexterity of:", self.__Dexterity)
            print("")
            print(Fore.LIGHTGREEN_EX + "( 3 ) Increase your vitality by 1")
            print(Fore.LIGHTGREEN_EX + "      Currently you have a basic vitality of:", self.__Vitality)
            print("")
            while True:
                choose = input("Choose: ")
                if choose == "1":
                    self.__Strength = self.__Strength + 1
                    print(Fore.LIGHTMAGENTA_EX + "Your strength increased by 1")
                    break
                elif choose == "2":
                    self.__Dexterity = self.__Dexterity + 1
                    print(Fore.LIGHTMAGENTA_EX + "Your dexterity increased by 1")
                    break
                elif choose == "3":
                    self.__Vitality = self.__Vitality + 1
                    print(Fore.LIGHTMAGENTA_EX + "Your vitality increased by 1")
                    break
                else:
                    print("")
                    print("Wrong input, try again...")
                    print("")
            if self.getLVL() % 2 == 0:
                print("")
                self.setSkill_points(self.getSkill_points() + 1)
                print("")
                skill_tree.Skill_Tree().getSkill_Tree(self)
            del self.Xp[:]
        if self.Lvl == 5:
            self.lvl_difficult = 1.4
        if self.Lvl == 10:
            self.lvl_difficult = 1.3
        if self.Lvl == 15:
            self.lvl_difficult = 1.2
        if self.Lvl == 20:
            self.lvl_difficult = 1.1
        return self.Xp
    #---------------------------------------------------------- LVL
    def getLVL(self):
        return self.Lvl
    # --------------------------------------------------------- Head
    def getHead(self):
        return self.Head
    # --------------------------------------------------------- Ear_left
    def getEar_Left(self):
        return self.Ear_left
    # --------------------------------------------------------- Ear_right
    def getEar_Right(self):
        return self.Ear_right
    # --------------------------------------------------------- Neck
    def getNeck(self):
        return self.Neck
    # --------------------------------------------------------- Body
    def getBody(self):
        return self.Body
    # --------------------------------------------------------- Hands
    def getHands(self):
        return self.Hands
    # --------------------------------------------------------- Finger_Left
    def getFinger_Left(self):
        return self.Finger_left
    # --------------------------------------------------------- Finger_Right
    def getFinger_Right(self):
        return self.Finger_right
    # --------------------------------------------------------- Legs
    def getLegs(self):
        return self.Legs
    # --------------------------------------------------------- Feet
    def getFeet(self):
        return self.Feet
    # --------------------------------------------------------- Blockchance
    def getBlockchance(self):
        a = self.Blockchance
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getCategory() == "Armor" and self.Hands[1][0].getBlockchance() >= 0:
            a += self.Hands[1][0].getBlockchance()
        return a
    def setBlockchance(self, new_Blockchance):
        self.Blockchance = new_Blockchance
    # --------------------------------------------------------- Vitality
    def getVitality(self):
        a = self.__Vitality
        # Head
        if len(self.Head) > 0 and self.Head[0].getBonus() > 0 and self.Head[0].getAttribute() == 1:
            a += self.Head[0].getBonus()
        # Head
        if len(self.Head) > 0 and self.Head[0].getBonus2() > 0 and self.Head[0].getAttribute2() == 1:
            a += self.Head[0].getBonus2()
        #-------------------------------------------------------------------------------------------------------
        # Ear left
        if len(self.Ear_left) > 0 and self.Ear_left[0].getBonus() > 0 and self.Ear_left[0].getAttribute() == 1:
            a += self.Ear_left[0].getBonus()
        # Ear left
        if len(self.Ear_left) > 0 and self.Ear_left[0].getBonus2() > 0 and self.Ear_left[0].getAttribute2() == 1:
            a += self.Ear_left[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Ear right
        if len(self.Ear_right) > 0 and self.Ear_right[0].getBonus() > 0 and self.Ear_right[0].getAttribute() == 1:
            a += self.Ear_right[0].getBonus()
        # Ear right
        if len(self.Ear_right) > 0 and self.Ear_right[0].getBonus2() > 0 and self.Ear_right[0].getAttribute2() == 1:
            a += self.Ear_right[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Neck
        if len(self.Neck) > 0 and self.Neck[0].getBonus() > 0 and self.Neck[0].getAttribute() == 1:
            a += self.Neck[0].getBonus()
        # Neck
        if len(self.Neck) > 0 and self.Neck[0].getBonus2() > 0 and self.Neck[0].getAttribute2() == 1:
            a += self.Neck[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Body
        if len(self.Body) > 0 and self.Body[0].getBonus() > 0 and self.Body[0].getAttribute() == 1:
            a += self.Body[0].getBonus()
        # Body
        if len(self.Body) > 0 and self.Body[0].getBonus2() > 0 and self.Body[0].getAttribute2() == 1:
            a += self.Body[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Finger left
        if len(self.Finger_left) > 0 and self.Finger_left[0].getBonus() > 0 and self.Finger_left[0].getAttribute() == 1:
            a += self.Finger_left[0].getBonus()
        # Finger left
        if len(self.Finger_left) > 0 and self.Finger_left[0].getBonus2() > 0 and self.Finger_left[0].getAttribute2() == 1:
            a += self.Finger_left[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Finger right
        if len(self.Finger_right) > 0 and self.Finger_right[0].getBonus() > 0 and self.Finger_right[0].getAttribute() == 1:
            a += self.Finger_right[0].getBonus()
        # Finger right
        if len(self.Finger_right) > 0 and self.Finger_right[0].getBonus2() > 0 and self.Finger_right[0].getAttribute2() == 1:
            a += self.Finger_right[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Legs
        if len(self.Legs) > 0 and self.Legs[0].getBonus() > 0 and self.Legs[0].getAttribute() == 1:
            a += self.Legs[0].getBonus()
        # Legs
        if len(self.Legs) > 0 and self.Legs[0].getBonus2() > 0 and self.Legs[0].getAttribute2() == 1:
            a += self.Legs[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Feet
        if len(self.Feet) > 0 and self.Feet[0].getBonus() > 0 and self.Feet[0].getAttribute() == 1:
            a += self.Feet[0].getBonus()
        # Feet
        if len(self.Feet) > 0 and self.Feet[0].getBonus2() > 0 and self.Feet[0].getAttribute2() == 1:
            a += self.Feet[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getBonus() > 0 and self.Hands[1][0].getAttribute() == 1:
            a += self.Hands[1][0].getBonus()
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getBonus2() > 0 and self.Hands[1][0].getAttribute2() == 1:
            a += self.Hands[1][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getBonus() > 0 and self.Hands[0][0].getAttribute() == 1:
            a += self.Hands[0][0].getBonus()
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getBonus2() > 0 and self.Hands[0][0].getAttribute2() == 1:
            a += self.Hands[0][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getBonus() > 0 and self.Hands[2][0].getAttribute() == 1:
            a += self.Hands[2][0].getBonus()
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getBonus2() > 0 and self.Hands[2][0].getAttribute2() == 1:
            a += self.Hands[2][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        return a
    def setVitality(self, new_Vitality):
        self.__Vitality = new_Vitality
    # ------------------------------------------------------------------- Dexterity
    def getDexterity(self):
        a = self.__Dexterity
        # Head
        if len(self.Head) > 0 and self.Head[0].getBonus() > 0 and self.Head[0].getAttribute() == 2:
            a += self.Head[0].getBonus()
        # Head
        if len(self.Head) > 0 and self.Head[0].getBonus2() > 0 and self.Head[0].getAttribute2() == 2:
            a += self.Head[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Ear left
        if len(self.Ear_left) > 0 and self.Ear_left[0].getBonus() > 0 and self.Ear_left[0].getAttribute() == 2:
            a += self.Ear_left[0].getBonus()
        # Ear left
        if len(self.Ear_left) > 0 and self.Ear_left[0].getBonus2() > 0 and self.Ear_left[0].getAttribute2() == 2:
            a += self.Ear_left[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Ear right
        if len(self.Ear_right) > 0 and self.Ear_right[0].getBonus() > 0 and self.Ear_right[0].getAttribute() == 2:
            a += self.Ear_right[0].getBonus()
        # Ear right
        if len(self.Ear_right) > 0 and self.Ear_right[0].getBonus2() > 0 and self.Ear_right[0].getAttribute2() == 2:
            a += self.Ear_right[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Neck
        if len(self.Neck) > 0 and self.Neck[0].getBonus() > 0 and self.Neck[0].getAttribute() == 2:
            a += self.Neck[0].getBonus()
        # Neck
        if len(self.Neck) > 0 and self.Neck[0].getBonus2() > 0 and self.Neck[0].getAttribute2() == 2:
            a += self.Neck[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Body
        if len(self.Body) > 0 and self.Body[0].getBonus() > 0 and self.Body[0].getAttribute() == 2:
            a += self.Body[0].getBonus()
        # Body
        if len(self.Body) > 0 and self.Body[0].getBonus2() > 0 and self.Body[0].getAttribute2() == 2:
            a += self.Body[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Finger left
        if len(self.Finger_left) > 0 and self.Finger_left[0].getBonus() > 0 and self.Finger_left[0].getAttribute() == 2:
            a += self.Finger_left[0].getBonus()
        # Finger left
        if len(self.Finger_left) > 0 and self.Finger_left[0].getBonus2() > 0 and self.Finger_left[0].getAttribute2() == 2:
            a += self.Finger_left[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Finger right
        if len(self.Finger_right) > 0 and self.Finger_right[0].getBonus() > 0 and self.Finger_right[0].getAttribute() == 2:
            a += self.Finger_right[0].getBonus()
        # Finger right
        if len(self.Finger_right) > 0 and self.Finger_right[0].getBonus2() > 0 and self.Finger_right[0].getAttribute2() == 2:
            a += self.Finger_right[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Legs
        if len(self.Legs) > 0 and self.Legs[0].getBonus() > 0 and self.Legs[0].getAttribute() == 2:
            a += self.Legs[0].getBonus()
        # Legs
        if len(self.Legs) > 0 and self.Legs[0].getBonus2() > 0 and self.Legs[0].getAttribute2() == 2:
            a += self.Legs[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Feet
        if len(self.Feet) > 0 and self.Feet[0].getBonus() > 0 and self.Feet[0].getAttribute() == 2:
            a += self.Feet[0].getBonus()
        # Feet
        if len(self.Feet) > 0 and self.Feet[0].getBonus2() > 0 and self.Feet[0].getAttribute2() == 2:
            a += self.Feet[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getBonus() > 0 and self.Hands[1][0].getAttribute() == 2:
            a += self.Hands[1][0].getBonus()
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getBonus2() > 0 and self.Hands[1][0].getAttribute2() == 2:
            a += self.Hands[1][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getBonus() > 0 and self.Hands[0][0].getAttribute() == 2:
            a += self.Hands[0][0].getBonus()
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getBonus2() > 0 and self.Hands[0][0].getAttribute2() == 2:
            a += self.Hands[0][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getBonus() > 0 and self.Hands[2][0].getAttribute() == 2:
            a += self.Hands[2][0].getBonus()
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getBonus2() > 0 and self.Hands[2][0].getAttribute2() == 2:
            a += self.Hands[2][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        return a
    def setDexterity(self, new_Dexterity):
        self.__Dexterity = new_Dexterity
    # ------------------------------------------------------------------- Strength
    def getStrength(self):
        a = self.__Strength
        # Head
        if len(self.Head) > 0 and self.Head[0].getBonus() > 0 and self.Head[0].getAttribute() == 3:
            a += self.Head[0].getBonus()
        # Head
        if len(self.Head) > 0 and self.Head[0].getBonus2() > 0 and self.Head[0].getAttribute2() == 3:
            a += self.Head[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Ear left
        if len(self.Ear_left) > 0 and self.Ear_left[0].getBonus() > 0 and self.Ear_left[0].getAttribute() == 3:
            a += self.Ear_left[0].getBonus()
        # Ear left
        if len(self.Ear_left) > 0 and self.Ear_left[0].getBonus2() > 0 and self.Ear_left[0].getAttribute2() == 3:
            a += self.Ear_left[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Ear right
        if len(self.Ear_right) > 0 and self.Ear_right[0].getBonus() > 0 and self.Ear_right[0].getAttribute() == 3:
            a += self.Ear_right[0].getBonus()
        # Ear right
        if len(self.Ear_right) > 0 and self.Ear_right[0].getBonus2() > 0 and self.Ear_right[0].getAttribute2() == 3:
            a += self.Ear_right[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Neck
        if len(self.Neck) > 0 and self.Neck[0].getBonus() > 0 and self.Neck[0].getAttribute() == 3:
            a += self.Neck[0].getBonus()
        # Neck
        if len(self.Neck) > 0 and self.Neck[0].getBonus2() > 0 and self.Neck[0].getAttribute2() == 3:
            a += self.Neck[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Body
        if len(self.Body) > 0 and self.Body[0].getBonus() > 0 and self.Body[0].getAttribute() == 3:
            a += self.Body[0].getBonus()
        # Body
        if len(self.Body) > 0 and self.Body[0].getBonus2() > 0 and self.Body[0].getAttribute2() == 3:
            a += self.Body[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Finger left
        if len(self.Finger_left) > 0 and self.Finger_left[0].getBonus() > 0 and self.Finger_left[0].getAttribute() == 3:
            a += self.Finger_left[0].getBonus()
        # Finger left
        if len(self.Finger_left) > 0 and self.Finger_left[0].getBonus2() > 0 and self.Finger_left[0].getAttribute2() == 3:
            a += self.Finger_left[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Finger right
        if len(self.Finger_right) > 0 and self.Finger_right[0].getBonus() > 0 and self.Finger_right[0].getAttribute() == 3:
            a += self.Finger_right[0].getBonus()
        # Finger right
        if len(self.Finger_right) > 0 and self.Finger_right[0].getBonus2() > 0 and self.Finger_right[0].getAttribute2() == 3:
            a += self.Finger_right[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Legs
        if len(self.Legs) > 0 and self.Legs[0].getBonus() > 0 and self.Legs[0].getAttribute() == 3:
            a += self.Legs[0].getBonus()
        # Legs
        if len(self.Legs) > 0 and self.Legs[0].getBonus2() > 0 and self.Legs[0].getAttribute2() == 3:
            a += self.Legs[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # Feet
        if len(self.Feet) > 0 and self.Feet[0].getBonus() > 0 and self.Feet[0].getAttribute() == 3:
            a += self.Feet[0].getBonus()
        # Feet
        if len(self.Feet) > 0 and self.Feet[0].getBonus2() > 0 and self.Feet[0].getAttribute2() == 3:
            a += self.Feet[0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getBonus() > 0 and self.Hands[1][0].getAttribute() == 3:
            a += self.Hands[1][0].getBonus()
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getBonus2() > 0 and self.Hands[1][0].getAttribute2() == 3:
            a += self.Hands[1][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getBonus() > 0 and self.Hands[0][0].getAttribute() == 3:
            a += self.Hands[0][0].getBonus()
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getBonus2() > 0 and self.Hands[0][0].getAttribute2() == 3:
            a += self.Hands[0][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getBonus() > 0 and self.Hands[2][0].getAttribute() == 3:
            a += self.Hands[2][0].getBonus()
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getBonus2() > 0 and self.Hands[2][0].getAttribute2() == 3:
            a += self.Hands[2][0].getBonus2()
        #----------------------------------------------------------------------------------------------------------
        return a
    def setStrength(self, new_Strength):
        self.__Strength = new_Strength
    # ------------------------------------------------------------------- Dmg
    def getDmg(self):
        a = self.Dmg
        # 1-Hand left
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getCategory() == "Weapon":
            a += self.Hands[1][0].getDmg()
        # 1-Hand right
        if len(self.Hands[0]) > 0 and self.Hands[0][0].getCategory() == "Weapon":
            a += self.Hands[0][0].getDmg()
        # 2-Hand
        if len(self.Hands[2]) > 0 and self.Hands[2][0].getCategory() == "Weapon":
            a += self.Hands[2][0].getDmg()
        a += self.getStrength()
        return a
    def setDmg(self, new_Dmg):
        self.Dmg = new_Dmg
    # ------------------------------------------------------------------- MaxHealth
    def getMaxHealth(self):
        if self.__Race == "Kro'L":
            self.__MaxHealth = round((self.getVitality() * 10) * 1.10)
        else:
            self.__MaxHealth = self.getVitality() * 10
        return self.__MaxHealth
    # ------------------------------------------------------------------- Health
    def getHealth(self):
        return self.__Health
    def setHealth(self, new_Health):
        self.__Health = new_Health
    # ------------------------------------------------------------------- get_Hit
    def get_Hit(self, dmg):
        a = self.getHealth()
        b = self.getHealth() - (dmg - self.getReduction(self.getReductionBonus()))
        if b > a:
            self.setHealth(self.getHealth())
        else:
            self.__Health = self.__Health - (dmg - self.getReduction(self.getReductionBonus()))
        if self.__Health <= 0:
            self.die()
    # ------------------------------------------------------------------- die
    def die(self):
        winsound.PlaySound("sounds\\tot.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        print("")
        print("")
        print(Style.BRIGHT + Fore.RED + "You have been killed, may your soul find peace in Valhalla!")
        sleep(5)
        clear()
        execl(sys.executable, sys.executable, *sys.argv)
    # ------------------------------------------------------------------- Armor
    def getArmor(self):
        a = self.Armor
        # Head
        if len(self.Head) > 0:
            a += self.Head[0].getArmor()
        # Body
        if len(self.Body) > 0:
            a += self.Body[0].getArmor()
        # Legs
        if len(self.Legs) > 0:
            a += self.Legs[0].getArmor()
        # Feet
        if len(self.Feet) > 0:
            a += self.Feet[0].getArmor()
        # Shield
        if len(self.Hands[1]) > 0 and self.Hands[1][0].getType() == "Shield":
            a += self.Hands[1][0].getArmor()
        return a

    def setArmor(self, new_Armor):
        self.Armor = new_Armor
    # ------------------------------------------------------------------- Reduction
    def getReductionBonus(self):
        return self.Reduction_bonus

    def setReductionBonus(self, new_ReductionBonus):
        self.Reduction_bonus = new_ReductionBonus

    def getReduction(self, number):
        self.Reduction = math.floor(self.getArmor() / number)
        return self.Reduction
    # ------------------------------------------------------------------- Inventory
    def getInventory(self):
        if len(self.Inventory) > 0:
            while True:
                print("")
                for (x, i) in enumerate(self.Inventory, start=1): #--- enumerate() numbers every Object in the Inventory
                    # Weapon no Bonus--------------------------------------------------------------------------------------------------------------
                    if i.getCategory() == "Weapon" and i.getBonus() == 0:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Value:", i.getValue(), "Taler")
                    # Weapon 1 Bonus---------------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Vitality +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Dexterity +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Strength +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    # Weapon 2 Bonus------------------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Vitality +", i.getBonus(), " Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Dexterity +", i.getBonus(), " Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Strength +", i.getBonus(), " Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                        #----------------------------------------------------------------------------
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Vitality +", i.getBonus(), " Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Vitality +", i.getBonus(), " Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Dexterity +", i.getBonus(), " Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                        #----------------------------------------------------------------------------
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Strength +", i.getBonus(), " Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Dexterity +", i.getBonus(), " Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Weapon" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), i.getHands(), "", i.getMinDmg(),"-", i.getMaxDmg(),"Dmg", "  Strength +", i.getBonus(), " Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    # Shield Nothing
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getBonus() == 0:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Value:", i.getValue(), "Taler")
                    # Shield 1 Bonus---------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() == 0:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Vitality +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() == 0:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Dexterity +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() == 0:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Strength +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    # Shield 2 Bonus---------------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Vitality +", i.getBonus(), " Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Vitality +", i.getBonus(), " Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 1 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Vitality +", i.getBonus(), " Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    #----------------------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Dexterity +", i.getBonus(), " Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Strength +", i.getBonus(), " Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Dexterity +", i.getBonus(), " Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                     #----------------------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Strength +", i.getBonus(), " Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 2 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Dexterity +", i.getBonus(), " Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getType() == "Shield" and i.getAttribute() == 3 and i.getBonus() > 0 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getName(), " Armor:", i.getArmor(), "", "Blockchance: ", i.getBlockchance(), "%", "  Strength +", i.getBonus(), " Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    # Armor Nothing-----------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() == 0:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Value:", i.getValue(), "Taler")
                    # Armor 1 Bonus-------------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Vitality +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Dexterity +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Strength +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    # Armor 2 Bonus-----------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Vitality +", i.getBonus(), "  Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Vitality +", i.getBonus(), "  Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Vitality +", i.getBonus(), "  Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    #----------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Dexterity +", i.getBonus(), "  Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Strength +", i.getBonus(), "  Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Dexterity +", i.getBonus(), "  Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    #----------------------------------------------------------------------
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Strength +", i.getBonus(), "  Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Dexterity +", i.getBonus(), "  Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Armor" and i.getNoShield() == "NoShield" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), "", "Armor:", i.getArmor(), "  Strength +", i.getBonus(), "  Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    # Jewellery 1 Bonus-----------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), "", " Vitality +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), "", " Dexterity +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() == 0:
                        print("(",x,")", i.getType(), "", " Strength +", i.getBonus(), "  Value:", i.getValue(), "Taler")
                    # Jewellery 2 Bonus------------------------------------------------------------------------------------------------------------ 
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), "", " Vitality +", i.getBonus(), "  Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), "", " Vitality +", i.getBonus(), "  Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 1 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), "", " Vitality +", i.getBonus(), "  Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    #------------------------------------------------------------
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), "", " Dexterity +", i.getBonus(), "  Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() > 0 and i.getAttribute2() == 1:
                        print("(",x,")", i.getType(), "", " Strength +", i.getBonus(), "  Vitality +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), "", " Dexterity +", i.getBonus(), "  Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    #------------------------------------------------------------
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), "", " Strength +", i.getBonus(), "  Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 2 and i.getBonus2() > 0 and i.getAttribute2() == 3:
                        print("(",x,")", i.getType(), "", " Dexterity +", i.getBonus(), "  Strength +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Jewellery" and i.getBonus() > 0 and i.getAttribute() == 3 and i.getBonus2() > 0 and i.getAttribute2() == 2:
                        print("(",x,")", i.getType(), "", " Strength +", i.getBonus(), "  Dexterity +", i.getBonus2(), "  Value:", i.getValue(), "Taler")
                    # Potion ----------------------------------------------------------------------------------------------------------------------
                    elif i.getCategory() == "Potion" and i.getName() == "Small_Potion":
                        if len(i.getStack()) > 0:
                            print("(",x,")", i.getName()," Quantity:",(len(i.getStack()) + 1), "", " Healing:", i.getSize(self.getRace()),"  Value:", i.getValue(), "Taler")
                        else:
                            print("(",x,")", i.getName()," Quantity: 1", "", " Healing:", i.getSize(self.getRace()),"  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Potion" and i.getName() == "Normal_Potion":
                        if len(i.getStack()) > 0:
                            print("(",x,")", i.getName()," Quantity:",(len(i.getStack()) + 1), "", " Healing:", i.getSize(self.getRace()),"  Value:", i.getValue(), "Taler")
                        else:
                            print("(",x,")", i.getName()," Quantity: 1", "", " Healing:", i.getSize(self.getRace()),"  Value:", i.getValue(), "Taler")
                    elif i.getCategory() == "Potion" and i.getName() == "Big_Potion":
                        if len(i.getStack()) > 0:
                            print("(",x,")", i.getName()," Quantity:",(len(i.getStack()) + 1), "", " Healing:", i.getSize(self.getRace()),"  Value:", i.getValue(), "Taler")
                        else:
                            print("(",x,")", i.getName()," Quantity: 1", "", " Healing:", i.getSize(self.getRace()),"  Value:", i.getValue(), "Taler")
                print("")
                print("")
                if len(self.Inventory) > 0:
                    choose = input("Do you want to use something? y/n: ")
                    if choose == "y":
                        print("")
                        number = input("Enter number: ")
                        for (x, i) in enumerate(self.Inventory, start=1):
                            # Potion -------------------------------------------------------------------------------------------------
                            # small potion------------------------------
                            if str(x) == number and i.getCategory() == "Potion" and i.getName() == "Small_Potion":
                                if len(i.getStack()) > 0:
                                    if self.getHealth() <= (self.getMaxHealth() - i.getSize(self.getRace())):
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(i.getSize(self.getRace())) + " life points")
                                        self.setHealth(self.getHealth() + i.getSize(self.getRace()))
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del i.getStack()[0]
                                        break
                                    elif self.getHealth() > (self.getMaxHealth() - i.getSize(self.getRace())) and self.getHealth() < self.getMaxHealth():
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(self.getMaxHealth() - self.getHealth()) + " life points")
                                        self.setHealth(self.getMaxHealth())
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del i.getStack()[0]
                                        break
                                    else:
                                        print("")
                                        print(Fore.GREEN + "Your life points are already full")
                                        print("")
                                        break
                                elif len(i.getStack()) == 0:
                                    if self.getHealth() <= (self.getMaxHealth() - i.getSize(self.getRace())):
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(i.getSize(self.getRace())) + " life points")
                                        self.setHealth(self.getHealth() + i.getSize(self.getRace()))
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del self.Inventory[x-1]
                                        break
                                    elif self.getHealth() > (self.getMaxHealth() - i.getSize(self.getRace())) and self.getHealth() < self.getMaxHealth():
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(self.getMaxHealth() - self.getHealth()) + " life points")
                                        self.setHealth(self.getMaxHealth())
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del self.Inventory[x-1]
                                        break
                                    else:
                                        print("")
                                        print(Fore.GREEN + "Your life points are already full")
                                        print("")
                                        break
                            # normal potion------------------------------
                            elif str(x) == number and i.getCategory() == "Potion" and i.getName() == "Normal_Potion":
                                if len(i.getStack()) > 0:
                                    if self.getHealth() <= (self.getMaxHealth() - i.getSize(self.getRace())):
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(i.getSize(self.getRace())) + " life points")
                                        self.setHealth(self.getHealth() + i.getSize(self.getRace()))
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del i.getStack()[0]
                                        break
                                    elif self.getHealth() > (self.getMaxHealth() - i.getSize(self.getRace())) and self.getHealth() < self.getMaxHealth():
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(self.getMaxHealth() - self.getHealth()) + " life points")
                                        self.setHealth(self.getMaxHealth())
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del i.getStack()[0]
                                        break
                                    else:
                                        print("")
                                        print(Fore.GREEN + "Your life points are already full")
                                        print("")
                                        break
                                elif len(i.getStack()) == 0:
                                    if self.getHealth() <= (self.getMaxHealth() - i.getSize(self.getRace())):
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(i.getSize(self.getRace())) + " life points")
                                        self.setHealth(self.getHealth() + i.getSize(self.getRace()))
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del self.Inventory[x-1]
                                        break
                                    elif self.getHealth() > (self.getMaxHealth() - i.getSize(self.getRace())) and self.getHealth() < self.getMaxHealth():
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(self.getMaxHealth() - self.getHealth()) + " life points")
                                        self.setHealth(self.getMaxHealth())
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del self.Inventory[x-1]
                                        break
                                    else:
                                        print("")
                                        print(Fore.GREEN + "Your life points are already full")
                                        print("")
                                        break
                            # big potion------------------------------
                            elif str(x) == number and i.getCategory() == "Potion" and i.getName() == "Big_Potion":
                                if len(i.getStack()) > 0:
                                    if self.getHealth() <= (self.getMaxHealth() - i.getSize(self.getRace())):
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(i.getSize(self.getRace())) + " life points")
                                        self.setHealth(self.getHealth() + i.getSize(self.getRace()))
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del i.getStack()[0]
                                        break
                                    elif self.getHealth() > (self.getMaxHealth() - i.getSize(self.getRace())) and self.getHealth() < self.getMaxHealth():
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(self.getMaxHealth() - self.getHealth()) + " life points")
                                        self.setHealth(self.getMaxHealth())
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del i.getStack()[0]
                                        break
                                    else:
                                        print("")
                                        print(Fore.GREEN + "Your life points are already full")
                                        print("")
                                        break
                                elif len(i.getStack()) == 0:
                                    if self.getHealth() <= (self.getMaxHealth() - i.getSize(self.getRace())):
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(i.getSize(self.getRace())) + " life points")
                                        self.setHealth(self.getHealth() + i.getSize(self.getRace()))
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del self.Inventory[x-1]
                                        break
                                    elif self.getHealth() > (self.getMaxHealth() - i.getSize(self.getRace())) and self.getHealth() < self.getMaxHealth():
                                        winsound.PlaySound("sounds\\plopp.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                                        print("")
                                        print(Fore.GREEN + "You regenerate " + str(self.getMaxHealth() - self.getHealth()) + " life points")
                                        self.setHealth(self.getMaxHealth())
                                        print("Yor actually Lifepoints are:", Fore.GREEN + str(self.getHealth()))
                                        print("")
                                        del self.Inventory[x-1]
                                        break
                                    else:
                                        print("")
                                        print(Fore.GREEN + "Your life points are already full")
                                        print("")
                                        break
                            # 1-Hand Weapon-----------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 0 and len(self.Hands[2]) == 0 and i.getHands() == "1-Hand":
                                self.Hands[0].append(i)
                                del self.Inventory[x-1]
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 0 and i.getHands() == "1-Hand":
                                self.Hands[1].append(i)
                                del self.Inventory[x-1]
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 1 and len(self.Hands[1]) == 1 and i.getHands() == "1-Hand":
                                while True:
                                    left_or_right = input("Do you want to carry the 1-handed weapon in your right or left hand?: ")
                                    if left_or_right == "right":
                                        self.Inventory.append(self.Hands[0][0])
                                        del self.Hands[0][0]
                                        self.Hands[0].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif left_or_right == "left":
                                        self.Inventory.append(self.Hands[1][0])
                                        del self.Hands[1][0]
                                        self.Hands[1].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    else:
                                        print("")
                                        print("Wrong input, try again...")
                                        print("")
                            # Allready wearing a 2-Hand Weapon
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 0 and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 1 and i.getHands() == "1-Hand":
                                while True:
                                    print("")
                                    yesno0 = input("You are already wearing a 2-Hand Weapon, do you want to replace it with the chosen 1-Hand Weapon? y/n: ")
                                    if yesno0 == "y":
                                        self.Inventory.append(self.Hands[2][0])
                                        del self.Hands[2][0]
                                        self.Hands[0].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno0 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Shield --------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Armor" and i.getType() == "Shield" and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 0:
                                self.Hands[1].append(i)
                                del self.Inventory[x-1]
                            # Allready wearing a Shield
                            elif str(x) == number and i.getCategory() == "Armor" and i.getType() == "Shield" and len(self.Hands[1]) == 1 and self.Hands[1][0].getType() == "Shield":
                                while True:
                                    print("")
                                    yesno1 = input("You are already wearing a Shield, do you want to replace it? y/n: ")
                                    if yesno1 == "y":
                                        self.Inventory.append(self.Hands[1][0])
                                        del self.Hands[1][0]
                                        self.Hands[1].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno1 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # allready wearing a 1-hand weapon
                            elif str(x) == number and i.getCategory() == "Armor" and i.getType() == "Shield" and len(self.Hands[1]) == 1 and self.Hands[1][0].getHands() == "1-Hand":
                                while True:
                                    print("")
                                    yesno2 = input("You are already wearing a 1-Hand Weapon, do you want to replace it? y/n: ")
                                    if yesno2 == "y":
                                        self.Inventory.append(self.Hands[1][0])
                                        del self.Hands[1][0]
                                        self.Hands[1].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno2 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Allready wearing a 2-Hand Weapon
                            elif str(x) == number and i.getCategory() == "Armor" and i.getType() == "Shield" and len(self.Hands[0]) == 0 and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 1:
                                while True:
                                    print("")
                                    yesno3 = input("You are already wearing a 2-Hand Weapon, do you want to replace it with the chosen Shield? y/n: ")
                                    if yesno3 == "y":
                                        self.Inventory.append(self.Hands[2][0])
                                        del self.Hands[2][0]
                                        self.Hands[1].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno3 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Weapon 2-Hand -------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 0 and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 0 and i.getHands() == "2-Hand":
                                self.Hands[2].append(i)
                                del self.Inventory[x-1]
                            # if right Hand allready used
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 1 and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 0 and i.getHands() == "2-Hand":
                                while True:
                                    print("")
                                    yesno6 = input("You are already wearing a 1-Hand Weapon, do you want to replace it with the chosen 2-Hand? y/n: ")
                                    if yesno6 == "y":
                                        self.Inventory.append(self.Hands[0][0])
                                        del self.Hands[0][0]
                                        self.Hands[2].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno6 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # if left Hand allready 1-Hand Weapon
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 0 and len(self.Hands[1]) == 1 and self.Hands[1][0].getCategory() == "Weapon" and self.Hands[1][0].getHands() == "1-Hand" and len(self.Hands[2]) == 0 and i.getHands() == "2-Hand":
                                while True:
                                    print("")
                                    yesno7 = input("You are already wearing a 1-Hand Weapon, do you want to replace it with the chosen 2-Hand? y/n: ")
                                    if yesno7 == "y":
                                        self.Inventory.append(self.Hands[1][0])
                                        del self.Hands[1][0]
                                        self.Hands[2].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno7 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # if left Hand allready a Shield
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 0 and len(self.Hands[1]) == 1 and self.Hands[1][0].getType() == "Shield" and len(self.Hands[2]) == 0 and i.getHands() == "2-Hand":
                                while True:
                                    print("")
                                    yesno8 = input("You are already wearing a Shield, do you want to replace it with the chosen 2-Hand? y/n: ")
                                    if yesno8 == "y":
                                        self.Inventory.append(self.Hands[1][0])
                                        del self.Hands[1][0]
                                        self.Hands[2].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno8 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # if left and right Hand allready used and enough space in the Inventory
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 1 and len(self.Hands[1]) == 1 and len(self.Hands[2]) == 0 and i.getHands() == "2-Hand" and len(self.Inventory) < self.Max_Length:
                                while True:
                                    print("")
                                    yesno9 = input("You are already use both Hands, do you want to replace them with the chosen 2-Hand? y/n: ")
                                    if yesno9 == "y":
                                        self.Hands[2].append(i)
                                        del self.Inventory[x-1]
                                        self.Inventory.append(self.Hands[0][0])
                                        del self.Hands[0][0]
                                        self.Inventory.append(self.Hands[1][0])
                                        del self.Hands[1][0]
                                        break
                                    elif yesno9 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # if left and right Hand allready used and not enough space in the Inventory
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 1 and len(self.Hands[1]) == 1 and len(self.Hands[2]) == 0 and i.getHands() == "2-Hand" and len(self.Inventory) == self.Max_Length:
                                while True:
                                    print("")
                                    yesno10 = input("You are already use both Hands, do you want to replace them with the chosen 2-Hand? y/n: ")
                                    if yesno10 == "y":
                                        print("")
                                        print("You have not enough space in your Inventory...")
                                        print("")
                                        break
                                    elif yesno10 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # if allready wearing a 2-Hand Weapon
                            elif str(x) == number and i.getCategory() == "Weapon" and len(self.Hands[0]) == 0 and len(self.Hands[1]) == 0 and len(self.Hands[2]) == 1 and i.getHands() == "2-Hand":
                                while True:
                                    print("")
                                    yesno11 = input("You are already wearing a 2-Hand Weapon, do you want to replace it with the chosen one? y/n: ")
                                    if yesno11 == "y":
                                        self.Inventory.append(self.Hands[2][0])
                                        del self.Hands[2][0]
                                        self.Hands[2].append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno11 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Head -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Head" and len(self.Head) == 0:
                                self.Head.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing a head
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Head" and len(self.Head) == 1:
                                while True:
                                    print("")
                                    yesno12 = input("You are already wearing a Headgear, do you want to replace it with the chosen one? y/n: ")
                                    if yesno12 == "y":
                                        self.Inventory.append(self.Head[0])
                                        del self.Head[0]
                                        self.Head.append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno12 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Body -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Body" and len(self.Body) == 0:
                                self.Body.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing a Body
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Body" and len(self.Body) == 1:
                                while True:
                                    print("")
                                    yesno13 = input("You are already wearing a Chest Armor, do you want to replace it with the chosen one? y/n: ")
                                    if yesno13 == "y":
                                        self.Inventory.append(self.Body[0])
                                        del self.Body[0]
                                        self.Body.append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno13 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Legs -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Legs" and len(self.Legs) == 0:
                                self.Legs.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Legs
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Legs" and len(self.Legs) == 1:
                                while True:
                                    print("")
                                    yesno14 = input("You are already wearing a Leggear, do you want to replace it with the chosen one? y/n: ")
                                    if yesno14 == "y":
                                        self.Inventory.append(self.Legs[0])
                                        del self.Legs[0]
                                        self.Legs.append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno14 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Feet -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Feet" and len(self.Feet) == 0:
                                self.Feet.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Feet
                            elif str(x) == number and i.getCategory() == "Armor" and i.getArea() == "Feet" and len(self.Feet) == 1:
                                while True:
                                    print("")
                                    yesno15 = input("You are already wearing a Feetgear, do you want to replace it with the chosen one? y/n: ")
                                    if yesno15 == "y":
                                        self.Inventory.append(self.Feet[0])
                                        del self.Feet[0]
                                        self.Feet.append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno15 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Neck -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Amulet" and len(self.Neck) == 0:
                                self.Neck.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Neck
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Amulet" and len(self.Neck) == 1:
                                while True:
                                    print("")
                                    yesno16 = input("You are already wearing a Amulet, do you want to replace it with the chosen one? y/n: ")
                                    if yesno16 == "y":
                                        self.Inventory.append(self.Neck[0])
                                        del self.Neck[0]
                                        self.Neck.append(i)
                                        del self.Inventory[x-1]
                                        break
                                    elif yesno16 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Ear right -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Earring" and len(self.Ear_right) == 0 and len(self.Ear_left) == 0:
                                self.Ear_right.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Ear right and Ear left is free
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Earring" and len(self.Ear_right) == 1 and len(self.Ear_left) == 0:
                                self.Ear_left.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Ear left and Ear right is free
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Earring" and len(self.Ear_right) == 0 and len(self.Ear_left) == 1:
                                self.Ear_right.append(i)
                                del self.Inventory[x-1]
                            # if allready both ears in use
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Earring" and len(self.Ear_right) == 1 and len(self.Ear_left) == 1:
                                while True:
                                    print("")
                                    yesno17 = input("You are already wearing two Earrings, do you want to replace one with the chosen one? y/n: ")
                                    if yesno17 == "y":
                                        print("")
                                        yesno18 = input("Which site you want to replace, left or right?: ")
                                        if yesno18 == "right":
                                            self.Inventory.append(self.Ear_right[0])
                                            del self.Ear_right[0]
                                            self.Ear_right.append(i)
                                            del self.Inventory[x-1]
                                            break
                                        elif yesno18 == "left":
                                            self.Inventory.append(self.Ear_left[0])
                                            del self.Ear_left[0]
                                            self.Ear_left.append(i)
                                            del self.Inventory[x-1]
                                            break
                                        else:
                                            print("")
                                            print("Wrong input, try again...")
                                            print("")
                                    elif yesno17 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                            # Ring right -----------------------------------------------------------------------------------------------------------------------
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Ring" and len(self.Finger_right) == 0 and len(self.Finger_left) == 0:
                                self.Finger_right.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Ring right and Ring left is free
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Ring" and len(self.Finger_right) == 1 and len(self.Finger_left) == 0:
                                self.Finger_left.append(i)
                                del self.Inventory[x-1]
                            # if allready wearing Ring left and Ring right is free
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Ring" and len(self.Finger_right) == 0 and len(self.Finger_left) == 1:
                                self.Finger_right.append(i)
                                del self.Inventory[x-1]
                            # if allready both Ring in use
                            elif str(x) == number and i.getCategory() == "Jewellery" and i.getArea() == "Ring" and len(self.Finger_right) == 1 and len(self.Finger_left) == 1:
                                while True:
                                    print("")
                                    yesno19 = input("You are already wearing two Rings, do you want to replace one with the chosen one? y/n: ")
                                    if yesno19 == "y":
                                        print("")
                                        yesno20 = input("Which site you want to replace, left or right?: ")
                                        if yesno20 == "right":
                                            self.Inventory.append(self.Finger_right[0])
                                            del self.Finger_right[0]
                                            self.Finger_right.append(i)
                                            del self.Inventory[x-1]
                                            break
                                        elif yesno20 == "left":
                                            self.Inventory.append(self.Finger_left[0])
                                            del self.Finger_left[0]
                                            self.Finger_left.append(i)
                                            del self.Inventory[x-1]
                                            break
                                        else:
                                            print("")
                                            print("Wrong input, try again...")
                                            print("")
                                    elif yesno19 == "n":
                                        break
                                    else:
                                        print("")    
                                        print("Wrong input, try again...")
                                        print("")
                    elif choose == "n":
                        print("")
                        yesno4 = input("Do you want to throw something away? y/n: ")
                        if yesno4 == "y":
                            print("")
                            yesno5 = input("Enter number: ")
                            for (x, i) in enumerate(self.Inventory, start=1):
                                if str(x) == yesno5:
                                    del self.Inventory[x-1]
                                    break
                        elif yesno4 == "n":
                            break
                        else:
                            print("Wrong input, try again...")
                    else:
                        print("")
                        print("Wrong input, try again...")
                        print("")
                else:
                    print("")
                    print("Your Inventory is empty.")
                    print("")
                    break
        else:
            print("")
            print("Your Inventory is empty.")
            print("")      

