import pygame

pygame.init()

window = pygame.display.set_mode([1024, 647])
window_title = pygame.display.set_caption("Futeball Pong")
res1 = 0
res2 = 0

field = pygame.image.load("assets/field.png")
chicken1 = pygame.image.load("assets/chicken.png")
chicken1_y = 270
chicken1_x = 30
chicken1_moveup = False
chicken1_movedown = False

chicken2 = pygame.image.load("assets/chicken2.png")
chicken2_y = 270
chicken2_x = 910
chicken2_moveup = False
chicken2_movedown = False

egg2 = pygame.image.load("assets/egg2.png")
egg2_x = 460
egg2_y = 250
ball_dir = 0.8
ball_dir_y = 0.7

def move_player():
    global chicken1_y

    if chicken1_moveup:
        chicken1_y -= 0.5
    if chicken1_movedown:
        chicken1_y += 0.5

    if chicken1_y <= 0:
        chicken1_y = 0
    elif chicken1_y >= 545:
        chicken1_y = 545

def move_player2():
    global chicken2_y

    if chicken2_moveup:
        chicken2_y -= 0.45
    if chicken2_movedown:
        chicken2_y += 0.45

    if chicken2_y <= 0:
        chicken2_y = 1
    elif chicken2_y >= 545:
        chicken2_y = 545

def move_egg():
    global egg2_x
    global egg2_y
    global ball_dir
    global ball_dir_y
    egg2_x += -ball_dir
    egg2_y += ball_dir_y

    if egg2_x < 90:
        if chicken1_y <= egg2_y + 124:
            if chicken1_y + 101 >= egg2_y:
                if chicken1_x >= egg2_x:
                    ball_dir *= -1

    if egg2_x > 845:
        if chicken2_y <= egg2_y + 124:
            if chicken2_y + 101 >= egg2_y:
                if chicken2_x <= egg2_x:
                    ball_dir *= -1

    if egg2_y >= 555:
        ball_dir_y *= -1
    if egg2_y <= 0:
        ball_dir_y *= -1

def draw():
    window.blit(field, (0, 0))
    window.blit(chicken1, (chicken1_x, chicken1_y))
    window.blit(chicken2, (chicken2_x, chicken2_y))
    window.blit(egg2, (egg2_x, egg2_y))

def placar():
    global egg2_x
    global res1, res2

    if egg2_x >= 950:
        res1 += 1
        print("Player1 = ", res1, " Machine = ", res2)
        egg2_x = 460
    if egg2_x <= -20:
        res2 += 1
        print("Player1 = ", res1, " Machine = ", res2)
        egg2_x = 460

loop = True
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                chicken1_moveup = True
            if events.key == pygame.K_s:
                chicken1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                chicken1_moveup = False
            if events.key == pygame.K_s:
                chicken1_movedown = False

    if chicken2_y > egg2_y:
        chicken2_movedown = False
        chicken2_moveup = True
    if chicken2_y < egg2_y:
        chicken2_movedown = True
        chicken2_moveup = False

    draw()
    move_egg()
    move_player()
    move_player2()
    placar()
    pygame.display.update()
