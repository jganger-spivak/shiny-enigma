import random
import pygame
from SpriteLib import UnravelSprite
from time import sleep, clock

class ModelMap:
    def __init__(self):
        self.world = []
        self.renderList = []
        self.size = 20
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.screen.fill((255, 255, 255))
        self.level = 0
        self.cloneCorrect = 0
    def gen(self, blank=" "):
        world = [blank] * self.size
        for i in range(0, self.size):
            world[i] = [blank] * self.size
        self.world.append(world)
    def show(self, debug = False):
        if debug:
            for i in self.world[self.level]:
                print(''.join(i))
            return
        else:
            self.culledRender()
    def flush(self):
        world = ["_"] * self.size
        for i in range(0, self.size):
            world[i] = ["_"] * self.size
        self.world[self.level] = world
    def fill(self, wall="%"):
        for i in self.world[self.level]:
            for idx, val in enumerate(i):
                if (idx == 0):
                    i[idx] = "%" #left side
                if (idx == len(i)-1):
                    i[idx] = "%" #right side
        for idx2, val2 in enumerate(self.world[self.level]):
            if (idx2 == 0 or idx2 == len(self.world[self.level])-1):
                topwall = [None] * len(self.world[self.level])
                for j in range(0, len(topwall)):
                    topwall[j] = "%"
                self.world[self.level][idx2] = topwall
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
            self.world[self.level][y][x] = char
        if (not spriteForDeletion == None):
            x = self.renderList[spriteForDeletion].x
            y = self.renderList[spriteForDeletion].y
            self.pl.cache = " "
            del self.renderList[spriteForDeletion]
        self.show(False)
    def graphicRender(self):
        start = clock()
        for  x, row in enumerate(self.world[self.level]):
            for y, tile in enumerate(row):
                for key in charTextures.keys():
                    if (self.world[self.level][y][x] == key):
                        self.screen.blit(charTextures[key], (x*10, y*10))
        pygame.display.update()
        print("Full Render Time: " + str(clock()-start))
    def culledRender(self):
        start = clock()
        for i in range(0, len(self.renderList)):
            if self.renderList[i].moved:
                if self.renderList[i].level == self.level:
                    #self.screen.blit(updateTex, (self.renderList[i].x*10, self.renderList[i].y*10))
                    #self.screen.blit(updateTex, (self.renderList[i].oldx*10, self.renderList[i].oldy*10))
                    #pygame.display.update()
                    #sleep(.05)
                    self.screen.blit(charTextures[self.renderList[i].char], (self.renderList[i].x*10, self.renderList[i].y*10))
                    self.screen.blit(charTextures[self.renderList[i].cache], (self.renderList[i].oldx*10, self.renderList[i].oldy*10))
                    self.renderList[i].moved = False
            elif not self.renderList[i].level == self.level:
                self.screen.blit(charTextures[self.renderList[i].cache], (self.renderList[i].oldx*10, self.renderList[i].oldy*10))
        pygame.display.update()
        print("Culled Render Time: " + str(clock()-start))

class Player(UnravelSprite):
    def __init__(self, x, y, XP):
        UnravelSprite.__init__(self, x, y, XP)
        self.maxhp = 10
        self.hp = 10
        self.char = "@"
        self.x = x
        self.y = y
        self.cache = "_"
    def move(self, x, y):
        if not self.map.world[self.level][y][x] == '#':
            self.translate(x, y)
            print(str(self.x) + "," + str(self.y))
        else: print("Invalid move.")

class Imp(UnravelSprite):
    def __init__(self, x, y, XP):
        UnravelSprite.__init__(self, x, y, XP)
        self.char = '#'
        self.cache = "_"
    def tick(self):
        targetx = self.x + random.randint(-1, 1)
        targety = self.y + random.randint(-1, 1)
        try:
            if (self.map.world[self.level][targety][targetx] == "%"):
                return True
            if (self.map.world[self.level][targety][targetx] == "O"):
                return True
            if (self.map.world[self.level][targety][targetx] == "#"):
                return True
            if (self.map.world[self.level][targety][targetx] == "@"):
                return True
            self.translate(targetx, targety)
        except IndexError:
            return True
        

world = ModelMap()
world.gen("_")
#world.fill()
pl = Player(1, 1, 0)
world.registerRender(pl)

charTextures = {}
charTextures["@"] = pygame.image.load('s_char.png').convert()
charTextures["%"] = pygame.image.load('wall.png').convert()
charTextures["_"] = pygame.image.load('s_grass.png').convert()
charTextures["#"] = pygame.image.load('s_imp.png').convert()
charTextures[" "] = pygame.image.load('s_default.png').convert()
updateTex = pygame.image.load('s_update.png').convert()

world.graphicRender()
world.render()



done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                world.render()
            if event.key == pygame.K_d:
                pl.move(pl.x + 1, pl.y)
                world.render()
            if event.key == pygame.K_a:
                pl.move(pl.x - 1, pl.y)
                world.render()
            if event.key == pygame.K_s:
                pl.move(pl.x, pl.y + 1)
                world.render()
            if event.key == pygame.K_w:
                pl.move(pl.x, pl.y - 1)
                world.render()
            if event.key == pygame.K_SPACE:
                world.level += 1
                pl.level += 1
                world.flush()
                world.render()
                print("Level: " + str(world.level))
            if event.key == pygame.K_LSHIFT:
                world.level -= 1
                pl.level -= 1
                world.flush()
                world.render()
                print("Level: " + str(world.level))
            if event.key == pygame.K_n:
                world.gen("_")
            if event.key == pygame.K_i:
                randx = random.randint(1, 19)
                randy = random.randint(1, 19)
                if (randx == 1 or randy == 1) or (world.world[world.level][randy][randx] == "%"):
                    print("Imp intersected player or wall")
                    #do nothing
                else:
                    world.registerRender(Imp(randx, randy, 1))
                    
exit()
