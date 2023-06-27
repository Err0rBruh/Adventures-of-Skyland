import pygame
from pygame.locals import *
import random
import sys

pygame.init()

modes = pygame.display.list_modes()
width1, height1 = modes[0]
width = width1 - 10
height = height1 - 63
rect_size = (50, 50)
x = 300
y = 300
w = 50
h = 50
w1 = 35
h1 = 35
screen = pygame.display.set_mode((width, height))
screen_width, screen_height = pygame.display.get_surface().get_size()
padding = 10
number = (100,)
number2 = (100,)
rect_size1 = (100, 100)
rect_size = (50, 50)
rect_down_pos = (screen_width - rect_size1[0] - padding, screen_height - rect_size1[1] - padding)
rect_left_pos = (screen_width - rect_size1[0] - padding - rect_size1[0], screen_height - rect_size1[1] - padding)
rect_right_pos = (screen_width - rect_size1[0] - padding, screen_height - rect_size1[1] - padding - rect_size1[1])
rect_up_pos = (screen_width - rect_size1[0] - padding - rect_size1[0], screen_height - rect_size1[1] - padding - rect_size1[1])
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
t = 20
bird3 = pygame.image.load('diamond.png')
bird3 = pygame.transform.scale(bird3, (w1, h1))
bird2 = pygame.image.load('enemy.png')
bird2 = pygame.transform.scale(bird2, (w, h))
bird = pygame.image.load('player.png')
bird = pygame.transform.scale(bird, (w, h))
image1 = pygame.image.load('skyland.png')
image1 = pygame.transform.scale(image1, (width, height))
image5 = pygame.image.load('intro.png')
image5 = pygame.transform.scale(image5, (width, height))
image6 = pygame.image.load('over.png')
image6 = pygame.transform.scale(image6, (width, height))
image11 = pygame.image.load('evening.png')
image11 = pygame.transform.scale(image11, (width, height))
image12 = pygame.image.load('night.png')
image12 = pygame.transform.scale(image12, (width, height))
score = 0
font = pygame.font.Font(None, 36)
text_render = font.render(str(score), True, (255, 255, 255))
text_rect = text_render.get_rect()

x2 = random.randint(50, 1000)
y2 = random.randint(50, 450)
w2 = 35
h2 = 20
x3 = random.randint(50, 1000)
y3 = random.randint(50, 450)
w3 = 10
h3 = 10
t2 = 30
t3 = 45
t1 = 23

pygame.display.set_caption("Adventures of Skyland")
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)

start_time = pygame.time.get_ticks()
delay = 160
intro = True
running = False
over = False

def reset_game():
    global score, x, y, x2, y2, x3, y3, start_time, delay
    score = 0
    x = 300
    y = 300
    x2 = random.randint(50, 1000)
    y2 = random.randint(50, 450)
    x3 = random.randint(50, 1000)
    y3 = random.randint(50, 450)
    start_time = pygame.time.get_ticks()
    delay = 100

def draw_text(surface, text, font, color, rect, center=True):
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    if center:
        text_rect.center = rect.center
    else:
        text_rect.topleft = rect.topleft
    surface.blit(text_render, text_rect)

while intro:
    screen.blit(image5, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            intro = False
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                running = True
                intro = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    while over:
        screen.blit(image6, (0, 0))
        draw_text(screen, " ", font, (255, 255, 255), screen.get_rect(), center=True)
        draw_text(screen, " ", font, (255, 255, 255), pygame.Rect(0, height - 50, width, 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP and event.key == K_SPACE:
                reset_game()
                running = True
                over = False
                break

    if running:
        screen.fill((0, 0, 0))
        screen.blit(image1, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(*rect_up_pos, *rect_size))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(*rect_left_pos, *rect_size))
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(*rect_right_pos, *rect_size))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(*rect_down_pos, *rect_size))
        screen.blit(bird3, (x3, y3))
        screen.blit(bird, (x, y))
        screen.blit(bird2, (x2, y2))
        draw_text(screen, str(score), font, (255, 255, 255), pygame.Rect(10, 10, 100, 50), center=False)
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= 28
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += 28
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= 28
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += 28
        if keys[pygame.K_p]:
            running = not running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.FINGERDOWN:
                touch_pos = (event.x * screen.get_width(), event.y * screen.get_height())
                if rect_left_pos.collidepoint(touch_pos):
                    x -= 28
                if rect_right_pos.collidepoint(touch_pos):
                    x += 28
                if rect_up_pos.collidepoint(touch_pos):
                    y -= 28
                if rect_down_pos.collidepoint(touch_pos):
                    y += 28

        if x < 0:
            x = width
        elif x > width:
            x = 0

        if y < 0:
            y = height
        elif y > height:
            y = 0

        if abs(x3 - x) < t2 and abs(y3 - y) < t3:
            x3 = random.randint(50, 1000)
            y3 = random.randint(50, 500)
            score += 1

        if score >= 15 and score < 35:
            image1 = pygame.image.load('evening.png')
            pygame.display.flip()
        if score >= 35 and score < 75:
            image1 = pygame.image.load('night.png')
            pygame.display.flip()
        if score >= 75:
            image1 = pygame.image.load('night.png')
            pygame.display.flip()
            delay = 50

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= delay:
            if x2 > x:
                x2 -= 24
            elif x2 < x:
                x2 += 24
            if y2 > y:
                y2 -= 23
            elif y2 < y:
                y2 += 23
            start_time = pygame.time.get_ticks()

        if abs(x2 - x) < t and abs(y2 - y) < t1:
            delay = 160
            image1 = pygame.image.load('skyland.png')
            image1 = pygame.transform.scale(image1, (width, height))
            over = True
            running = False

pygame.quit() 
