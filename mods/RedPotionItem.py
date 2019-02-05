from SpriteLib import Sprite
import random

class RedPotionItem(Sprite):
    def __init__(self, x, y, XP):
        Sprite.__init__(self, x, y, XP)
        self.char = "!"
        self.XP = 0
        self.hasInit = False
        self.isInteractive = True
        self.title = "  Health Potion +5  "
        self.x = 3
        self.y = 3
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
        pl.hp += 5
        if pl.hp > pl.maxhp:
            pl.hp = pl.maxhp
