from SpriteLib import Sprite

class TestObjEnemy(Sprite):
    def __init__(self, x, y, XP):
        Sprite.__init__(self, x, y, XP)
        self.char = "$"
        self.x = 2
        self.y = 2
        self.XP = 5
        self.hp = 30
        self.dmg = 3
        self.isEnemy = True
    def info():
        return ["$", 2, 2, 5]
    
