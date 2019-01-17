class Sprite:
  def __init__(self, x, y, XP):
    self.x = x
    self.y = y
    self.char = " "
    self.XP = XP
    self.map = None
    self.cache = " "
    self.cachex = x
    self.cachey = y
    self.isXP = False
  def translate(self, x, y):
    self.map.world[self.cachey][self.cachex] = self.cache
    self.cachex = x
    self.cachey = y
    self.cache = self.map.world[y][x]
    self.x = x
    self.y = y
  def convertXP(self):
    self.char = "*"
    self.isXP = True
  def tick(self):
    2+2
    #do nothing in particular, at the moment
