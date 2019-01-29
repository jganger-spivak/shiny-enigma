#ENGINE CODE HERE =============================================================================================================================================================================================================
import random
import time
import importlib
import os
import sys
import pickle
root = os.path.dirname(__file__)
sys.path.append(root + "\\mods\\")
class NotWorld:
  def __init__(self):
    self.world = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
    self.renderList = []
    self.size = 3
    self.pl = None
  def gen(self, size):
    world = [" "] * size
    for i in range(0, len(world)):
      world[i] = [" "] * size
    self.world = world
    self.size = size
    return world
  def show(self):
    for i in self.world:
      print(''.join(i))
  def fill(self):
    for i in self.world:
      for idx, val in enumerate(i):
        if (idx == 0):
          i[idx] = "%" #left side
        if (idx == len(i)-1):
          i[idx] = "%" #right side
    for idx2, val2 in enumerate(self.world):
      if (idx2 == 0 or idx2 == len(self.world)-1):
        topwall = [None] * len(self.world)
        for j in range(0, len(topwall)):
          topwall[j] = "%"
        self.world[idx2] = topwall
    noisebase = ((self.size-2)*(self.size-2)) / 8
    for i in range(0, int(noisebase)):
      randx = random.randint(1, self.size-1)
      randy = random.randint(1, self.size-1)
      if (randx == 1 or randy == 1) or (self.world[randy][randx] == "%"):
        print("Bush intersected player or wall")
      else:
        self.world[randy][randx] = "O"
  def registerRender(self, sprite):
    self.renderList.append(sprite)
    sprite.map = self
  def render(self):
    spriteForDeletion = None
    renderListLength = len(self.renderList)
    for s in range(0, renderListLength):
      if (self.renderList[s].pickedUp):
        spriteForDeletion = s
      if (not self.renderList[s].isXP):
        self.renderList[s].tick()
      x = self.renderList[s].x
      y = self.renderList[s].y
      char = self.renderList[s].char
      self.world[y][x] = char
    if (not spriteForDeletion == None):
      x = self.renderList[spriteForDeletion].x
      y = self.renderList[spriteForDeletion].y
      self.pl.cache = " "
      del self.renderList[spriteForDeletion]
    self.show()

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

    
def diceRoll(num):
  sum = 0
  for n in range(0, num):
    sum += random.randint(1, 6)
  return sum
#ACTUAL GAME CODE =============================================================================================================================================================================================================
class Player(Sprite):
  def __init__(self, x, y, XP):
    Sprite.__init__(self, x, y, XP)
    self.maxhp = 10
    self.hp = 10
    self.char = "@"
    self.basedmg = 1
    self.atk = 1
    self.atkplus = 0
    self.dfcplus = 0
    self.dfc = 1
    self.xp = 0
    self.xpNeeded = 10
    self.level = 1
    self.inventory = []
  def move(self, x, y):
    if (self.map.world[y][x] == "%"):
      print("Invalid move. Returning...")
      self.map.show()
      return True
    if (self.map.world[y][x] == "O"):
      print("Invalid move. Returning...")
      self.map.show()
      return True
    for e in enemyList:
      if (self.map.world[y][x] == e):
        battle(x, y)
        #Place battle code here
        self.map.show()
        return True
    for e in interactList:
      if (self.map.world[y][x] == e):
        interact(x, y)
        self.map.show()
    if (self.map.world[y][x] == "*"):
      impObjIndex = 0
      for i in range(0, len(self.map.renderList)):
        if (self.map.renderList[i].x == x):
          if (self.map.renderList[i].y == y):
            impObjIndex = i
      self.giveXP(self.map.renderList[impObjIndex].XP)
      print(str(self.map.renderList[impObjIndex].XP) + " xp given!")
      del self.map.renderList[impObjIndex]
      self.map.world[y][x] = " "
      self.map.show()
    if (self.map.world[y][x] == "@"):
      print("You're already here. Returning...")
      self.map.show()
      return True
    self.translate(x, y)
    self.map.render()
    return False
  def tick(self):
    if (self.hp <= 0):
      print("    GAME  OVER    ")
      exit()
  def levelUp(self):
    print("====================")
    print("=     LEVEL UP     =")
    print("====================")
    print("Pick stat to upgrade")
    print("    ATK  HP  DFC    ")
    cmd = input(": ")
    if (cmd == "atk"):
      self.atk += 1
    if (cmd == "dfc"):
      self.dfc += 1
    if (cmd == "hp"):
      self.maxhp += 5
      self.hp = self.maxhp
    print("====================")
    print("=    New Stats:    =")
    print("====================")
    print("       ATK: " + str(self.atk) + "       ")
    print("       DFC: " + str(self.dfc) + "       ")
    print("       HP: " + str(self.maxhp) + "       ")
    self.level += 1
  def giveXP(self, num):
    self.xp += num
    if (self.xp >= self.xpNeeded):
      self.levelUp()
      self.xp -= self.xpNeeded
      self.xpNeeded *= self.level
  def save(self, num):
    save = []
    save.append(self.level)
    save.append(self.atk)
    save.append(self.dfc)
    save.append(self.hp)
    save.append(self.maxhp)
    save.append(self.xp)
    save.append(len(self.inventory))
    
    savefile = open(".\\saves\\" + str(num) + ".txt", "w")
    savefile.write(str(save))
    savefile.close()
    for i in range(0, len(self.inventory)):
      invfile = open(".\\saves\\" + str(num) + "inv" + str(i) + ".dat", "wb")
      pickle.dump(self.inventory[i], invfile)
      invfile.close()
  def load(self, num):
    save = []
    savefile = open(".\\saves\\" + str(num) + ".txt", "r")
    savestr = savefile.read()
    save = savestr.replace("[", "").replace("]", "").replace(" ", "").split(",")
    for s in range(0, len(save)):
      save[s] = int(save[s])
    self.level = save[0]
    self.atk = save[1]
    self.dfc = save[2]
    self.hp = save[3]
    self.maxhp = save[4]
    self.xp = save[5]
    self.xpNeeded = 10 * save[0]
    for i in range(0, save[6]):
      invfile = open(".\\saves\\" + str(num) + "inv" + str(i) + ".dat", "rb")
      pl.pickup(pickle.load(invfile))
      pl.inventory[i].loaded(pl)
      invfile.close()
  def pickup(self, obj):
    self.inventory.append(obj)
class Imp(Sprite):
  def __init__(self, x, y, XP):
    Sprite.__init__(self, x, y, XP)
    self.hp = 10
    self.dmg = 1
    self.char = "#"
  def tick(self):
    
    targetx = self.x + random.randint(-1, 1)
    targety = self.y + random.randint(-1, 1)
    if (self.map.world[targety][targetx] == "%"):
      return True
    if (self.map.world[targety][targetx] == "O"):
      return True
    if (self.map.world[targety][targetx] == "#"):
      return True
    self.translate(targetx, targety)

world = NotWorld()
world.gen(20)
world.fill()
imps = []
for i in range(0, 10):
  randx = random.randint(1, 19)
  randy = random.randint(1, 19)
  if (randx == 1 or randy == 1) or (world.world[randy][randx] == "%"):
    print("Imp intersected player or wall")
    #do nothing
  else:
    imps.append(Imp(randx, randy, 1))
pl = Player(1, 1, 0)
world.pl = pl
for i in range(0, len(imps)):
  world.registerRender(imps[i])

enemyList = ['#']
interactList = []
fh = open('modlist.txt', "r")
for line in fh:
  i = importlib.import_module(line.replace('\n', '').replace('.py', ''))
  info = eval("i." + line.replace('\n', '').replace('.py', '') + ".info()")
  modobj = eval("i." + line.replace('\n', '').replace('.py', '') + "(" + str(info[1]) + "," + str(info[2]) + "," + str(info[3]) + ")")
  world.registerRender(modobj)
  if (modobj.isEnemy):
    enemyList.append(modobj.char)
  if (modobj.isInteractive):
    interactList.append(modobj.char)

world.registerRender(pl)







def handleInput():
    cmd = input(": ")
    if (cmd == "w"):
      pl.move(pl.x, pl.y - 1)
    
    if (cmd == "s"):
      pl.move(pl.x, pl.y + 1)
    
    if (cmd == "a"):
      pl.move(pl.x - 1, pl.y)
    
    if (cmd == "d"):
      pl.move(pl.x + 1, pl.y)
    if (cmd == ""):
      world.render()
    if (cmd == "imps"):
      print(len(imps))
      world.show() 
    if (cmd == "console"):
      print("Type handleInput() to return to game")
      print(eval(input(">")))
    if(cmd == "stats"):
      stats()
      input()
      world.show()
    if (cmd == "exit"):
      exit()
    if (cmd == "help"):
      help()
      input()
      world.show()
    if (cmd == "save"):
      stats()
      pl.save(input("  Enter save slot:  \n"))
      world.show()
    if (cmd == "load"):
      pl.load(input("  Enter load slot:  \n"))
      stats()
      inventory()
      input()
      world.show()
    if (cmd == "inv"):
      inventory()
    if (cmd.split(" ")[0] == "use"):
      pl.inventory[int(cmd.split(" ")[1])].use(pl)
      if not pl.inventory[int(cmd.split(" ")[1])].isEquippable:
        del pl.inventory[int(cmd.split(" ")[1])]
    handleInput()
def battle(objx, objy):
  impObjIndex = 0
  for i in range(0, len(world.renderList)):
    if (world.renderList[i].x == objx):
      if (world.renderList[i].y == objy):
        impObjIndex = i
  print("====================")
  print("=      BATTLE      =")
  print("====================")
  print("=     Enemy HP     =")
  print("=        " + str(world.renderList[impObjIndex].hp) + "         =")
  print("=     PlayerHP     =")
  print("=        " + str(pl.hp) + "         =")
  print("\n\n\n\n\n\n\n\n")
  cmd = input("=    ATK    RUN    =\n")
  print("\n\n\n\n")
  if (cmd == "run"):
    atkDmg = diceRoll(pl.atk)
    if (atkDmg*3 >= world.renderList[impObjIndex].hp):
        print("Ran away successfully")
        return
    else:
        print("Failed. -1*lvl HP.")
        pl.hp -= pl.level
  if (cmd == "atk"):
    atkDmg = diceRoll(pl.atk) + pl.atkplus
    dfcBlock = diceRoll(pl.dfc) -1
    if ((world.renderList[impObjIndex].dmg - dfcBlock) >= 0):
      pl.hp -= world.renderList[impObjIndex].dmg - dfcBlock
      print("Enemy did " + str(world.renderList[impObjIndex].dmg - dfcBlock) + " damage.")
    world.renderList[impObjIndex].hp -= pl.basedmg + atkDmg
    print("Player did " + str(pl.basedmg + atkDmg) + " damage.")
    if (world.renderList[impObjIndex].hp <= 0):
      world.renderList[impObjIndex].convertXP()
      world.render()
      return
    battle(objx, objy)
  else:
    battle(objx, objy)
def interact(objx, objy):
  objIndex = 0
  for i in range(0, len(world.renderList)):
    if (world.renderList[i].x == objx):
      if (world.renderList[i].y == objy):
        world.renderList[i].handleInteract(pl)
def stats():
  print("      LEVEL: " + str(pl.level) + "      ")
  print("       ATK: " + str(pl.atk) + "d+" + str(pl.atkplus) + "     ")
  print("       DFC: " + str(pl.dfc) + "d+" + str(pl.dfcplus) + "     ")
  print("       HP: " + str(pl.hp) + "       ")
  print("       XP: " + str(pl.xp) + "       ")
  print("XP to next level:" + str(pl.xpNeeded - pl.xp) + "   ")

def help():
  print("====================")
  print("=       HELP       =")
  print("====================")
  print("      Commands      ")
  print("  w: Move Up")
  print("  a: Move Left")
  print("  s: Move Down")
  print("  d: Move Right")
  print("stats: Displays Stats")
  print("help: This window")
  print("console: Evident")
  print("====================")
  print("=    In Battle:    =")
  print("====================")
  print("  atk: Roll Attack")
  print("run:Attempt to flee")
  print("====================")
  print("     (c) 2019       ")
def inventory():
  print("====================")
  print("=    INVENTORY:    =")
  print("====================")
  for i in range(0, len(pl.inventory)):
    print(str(i) + ": "  + pl.inventory[i].title)
  print("====================")
  
world.render()
handleInput()
