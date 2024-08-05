import pygame
import random
pygame.init()
sw=800
sh=600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Animation Effect")
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
numobjs = 10
objs = []
for _ in range(numobjs):
    x = random.randint(50,sw-50)
    y = random.randint(50,sh-50)
    radius = random.randint(10,30)
    color = random.choice([RED, GREEN, BLUE])
    xspeed = random.randint(-5,5)
    yspeed = random.randint(-5,5)
    objs.append({"x":x,"y":y, "radius":radius, "color":color,"xspeed":xspeed,"yspeed":yspeed})
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    screen.fill(WHITE)
    for o in objs:
        o["x"] += o["xspeed"]
        o["y"] += o["yspeed"]
        if o["x"] - o["radius"] < 0 or o["x"] + o["radius"] > sw:
            o["xspeed"] = -o["xspeed"]
        if o["y"] - o["radius"] < 0 or o["y"] + o["radius"] > sh:
            o["yspeed"] = -o["yspeed"]
        pygame.draw.circle(screen, o["color"], (o["x"], o["y"]), o["radius"])
    pygame.display.flip()

    clock.tick(60)
pygame.quit()