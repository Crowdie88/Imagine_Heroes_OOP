import items
import random
# sounds
import winsound
# color und styles
from colorama import init, Fore, Back, Style

class Enemy:
    def __init__(self, lp, mindmg, maxdmg, name, attacks, xp, taler):
        self.Lp = lp
        self.Name = name
        self.Attacks = attacks
        self.Xp = xp
        self.Taler = taler
        self.MinDmg = mindmg
        self.MaxDmg = maxdmg
    def getDmg(self):
        dice_dmg = random.randint(self.MinDmg, self.MaxDmg)
        return dice_dmg
    def getXP(self, player):
        for i in range(self.Xp):
            player.Xp.append("")
            player.getXP()


class Goblin(Enemy):
    def __init__(self):
        Enemy.__init__(self, 18, 2, 5, "Goblin", 1, 1, 1)
    def get_hit(self, dmg, player):
        self.Lp = self.Lp - dmg
        if self.Lp <= 0:
            self.die(player)
    def die(self, player):
        player.setTaler(player.getTaler() + self.Taler)
        print(self.Name, Fore.RED + "has been killed\n")
        print(Fore.LIGHTGREEN_EX + "You get", Fore.LIGHTGREEN_EX + str(self.Xp), Fore.LIGHTGREEN_EX + "xp")
        self.getXP(player)
        print(self.Name," has dropped ", self.Taler, Fore.YELLOW + "Taler")
        dice = random.randint(1,100)
        if dice >= 45 and dice <= 60:
            player.push(self.drop())
            print(self.Name," has dropped an", Fore.LIGHTMAGENTA_EX + "Item")
        print("")
    def drop(self):
        item = random.choice(items.basic_item_list)
        return item
