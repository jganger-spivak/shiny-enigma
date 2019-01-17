from SpriteLib import Sprite

class TestObj(Sprite):
    def __init__(self, x, y, XP):
        Sprite.__init__(self, x, y, XP)
        self.char = "$"
        self.info = "TestObj(2, 2, 0)"


