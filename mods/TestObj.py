from SpriteLib import Sprite

class TestObj(Sprite):
    def __init__(self, x, y, XP):
        Sprite.__init__(self, x, y, XP)
        self.char = "$"
        self.x = 2
        self.y = 2
        self.XP = 0
    def info():
        return ["$", 2, 2, 0]
    
