import pygame
import random
class Meteorut:
    def __init__(self, x, y, w, h, filename, speed):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])

class Litak:
    def __init__(self, x, y, w, h, filename, speed):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
    
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])
pygame.init()
bomba = []
x = 20
y = 20
for i in range(10):
    bomba.append( Meteorut(x, y, 37, 74, "meteor.png", 2))
    x += 100
    y += -50

pygame.init() 
toy = Litak(170, 250, 37, 74, "plain.png", 0)

screen = pygame.display.set_mode((500, 500,)) 
fps = pygame.time.Clock()


loseTable = pygame.font.Font(None, 68).render("ТИ ПРОГРАВ!!!", True, (255, 0, 0))
winTable = pygame.font.Font(None, 68).render("ТИ ПЕРЕМІГ!!!", True, (0, 0, 56))

game = True


while game:
    for i in range( len(bomba) ):
        bomba[i].rect.y += bomba[i].speed
    screen.fill((2, 0, 55))
    for i in range( len(bomba) ):
        bomba[i].draw(screen)
        toy.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                toy.speed = 1
            if event.key == pygame.K_a:
                toy.speed = -1

        

    toy.rect.x +=  toy.speed 
    
    
    pygame.display.flip()
    for i in range( len(bomba) ):
        if bomba[i].rect.y > 500:
            bomba[i].rect.y = 0
            bomba[i].rect.x = random.randint(0, 400)

        if bomba[i].rect.colliderect(toy.rect):
              toy.speed *= -1
              bomba.pop(i)
              game = False
              screen.blit(loseTable, [180, 250])
              pygame.display.flip()
              break

    fps.tick(60)

