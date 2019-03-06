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
    self.moved = False
    self.oldx = x
    self.oldy = y
  def translate(self, x, y):
    self.oldx = self.x
    self.oldy = self.y
    self.map.world[self.cachey][self.cachex] = self.cache
    self.cachex = x
    self.cachey = y
    self.cache = self.map.world[y][x]
    self.x = x
    self.y = y
    self.moved = True
  def convertXP(self):
    self.char = "*"
    self.isXP = True
  def tick(self):
    pass
    #do nothing in particular, at the moment
  def handleInteract(self, pl):
    pass
    #Still do nothing, unless needed
  def use(self, pl):
    pass
  def loaded(self, pl):
    pass
    #This isn't the same as init. Just something to refresh pl values with when loaded from file.

#UNRAVEL STUFF #########################################################

class UnravelSprite:
  def __init__(self, x, y, XP):
    self.x = x
    self.y = y
    self.level = 0
    self.char = " "
    self.XP = XP
    self.map = None
    self.cache = " "
    self.cachex = x
    self.cachey = y
    self.cachelevel = self.level
    self.isXP = False
    self.isEnemy = False
    self.isInteractive = False
    self.isEquippable = False
    self.equipped = False
    self.title = "GenericSprite"
    self.pickedUp = False
    self.moved = False
    self.oldx = x
    self.oldy = y
  def translate(self, x, y):
    if (x < 1) or (y < 1):
      return
    elif (x > 18) or (y > 18):
      return
    self.oldx = self.x
    self.oldy = self.y
    self.map.world[self.level][self.cachey][self.cachex] = self.cache
    self.cachex = x
    self.cachey = y
    self.cache = self.map.world[self.level][y][x]
    self.cachelevel = self.level
    self.x = x
    self.y = y
    self.moved = True
  def convertXP(self):
    self.char = "*"
    self.isXP = True
  def tick(self):
    pass
    #do nothing in particular, at the moment
  def handleInteract(self, pl):
    pass
    #Still do nothing, unless needed
  def use(self, pl):
    pass
  def loaded(self, pl):
    pass
    #This isn't the same as init. Just something to refresh pl values with when loaded from file.
