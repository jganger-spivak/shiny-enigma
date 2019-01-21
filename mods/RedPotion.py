from SpriteLib import Sprite
import random

class RedPotion(Sprite):
    def __init__(self, x, y, XP):
        Sprite.__init__(self, x, y, XP)
        self.char = "+"
        self.XP = 0
        self.hasInit = False
        self.isInteractive = True
    def info():
        return ["nope", 0, 0, 0]
    def tick(self):
        if not self.hasInit:
            randx = random.randint(1, 19)
            randy = random.randint(1, 19)
            while not self.hasInit:
                if (randx == 1 or randy == 1) or (self.map.world[randy][randx] == "%"):
                    2+2 #Do nothing
                else:
                    self.translate(randx, randy)
                    self.hasInit = True
    def handleInteract(self, pl):
        pl.hp += 5
        if pl.hp > pl.maxhp:
            pl.hp = pl.maxhp
        
