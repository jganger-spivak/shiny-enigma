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
    self.isEnemy = False
    self.isInteractive = False
    self.isEquippable = False
    self.equipped = False
    self.title = "GenericSprite"
    self.pickedUp = False
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
  def handleInteract(self, pl):
    2+2
    #Still do nothing, unless needed
  def use(self, pl):
    2+2
  def loaded(self, pl):
    2+2
    #This isn't the same as init. Just something to refresh pl values with when loaded from file.
