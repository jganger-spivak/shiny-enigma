from SpriteLib import Sprite
import random

class IronSword(Sprite):
    def __init__(self, x, y, XP):
        Sprite.__init__(self, x, y, XP)
        self.char = "!"
        self.XP = 0
        self.hasInit = False
        self.isInteractive = True
        self.isEquippable = True
        self.equipped = False
        self.title = "   Iron Sword +2"
    def info():
        return ["nope", 0, 0, 0]
        #This doesn't actually mean anything, just has to be valid to instansiate the class

    def tick(self):
        if not self.hasInit:
            while not self.hasInit:
                randx = random.randint(1, 19)
                randy = random.randint(1, 19)
                if (self.map.world[randy][randx] == " "):
                    self.translate(randx, randy)
                    self.hasInit = True
    def handleInteract(self, pl):
        pl.pickup(self)
        self.pickedUp = True
    def use(self, pl):
        if not self.equipped:
            pl.atkplus += 2
            self.equipped = not self.equipped
            self.title = "E  Iron Sword +2    "
        else:
            pl.atkplus -= 2
            self.equipped = not self.equipped
            self.title = "   Iron Sword +2    "
    def loaded(self, pl):
        if self.equipped:
            pl.atkplus += 2
