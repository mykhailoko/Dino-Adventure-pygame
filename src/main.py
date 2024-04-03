import pygame
import os
import random 
from enum import Enum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

pygame.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERES'] = '1' 
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width, screen_height - 60

SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width
SCREEN = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Dino Adventure")

from assets import *
from dinosaur import *
from obstacles import *
from button import *

pygame.mixer.music.load(MAIN_MENU_MUSIC)
pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость музыки (от 0 до 1)
pygame.mixer.music.play(-1)  # -1 означает,что музыка будет воспроизводиться в цикле бесконечно 
    

class BackgroundType(Enum):
    DEFAULT = 0
    WINTER = 1
    BEACH = 2
    ZOMBI = 3

class ForegroundType(Enum):
    BLACK = 0
    WHITE = 1

class ObstaclesType(Enum):
    DEFAULT = 0
    WINTER = 1
    BEACH = 2
    ZOMBI = 3

class LevelType(Enum):
    DEFAULT = 0
    WINTER = 1
    BEACH = 2
    ZOMBI = 3


def main_background(background_type):
    if background_type == BackgroundType.DEFAULT:
        return CLASSIC1, CLASSIC2
    elif background_type == BackgroundType.WINTER:
        return WINTER1, WINTER2, WINTER3
    elif background_type == BackgroundType.BEACH:
        return BEACH1, BEACH2, BEACH3
    elif background_type == BackgroundType.ZOMBI:
        return ZOMBI1, ZOMBI2, ZOMBI3
    
def foreground(foreground_type):
    if foreground_type == ForegroundType.BLACK:
        return (0, 0, 0)
    elif foreground_type == ForegroundType.WHITE:
        return (255, 255, 255)
    
def obstacles(obstacles_type):
    if obstacles_type == ObstaclesType.DEFAULT:
        return SMALL_CACTUS, LARGE_CACTUS, BIRD
    elif obstacles_type == ObstaclesType.WINTER:
        return SMALL_CACTUS_WINTER, LARGE_CACTUS_WINTER, BIRD_WINTER
    elif obstacles_type == ObstaclesType.BEACH:
        return LARGE_BOARDS, LARGE_TREES, BIRD_BEACH
    elif obstacles_type == ObstaclesType.ZOMBI:
        return LARGE_GRAVES, ZOMBI, BAT
    
def level(level_type):
    if level_type == LevelType.DEFAULT:
        return "main"
    elif level_type == LevelType.WINTER:
        return "main_winter"
    elif level_type == LevelType.BEACH:
        return "main_beach"
    elif level_type == LevelType.ZOMBI:
        return "main_zombi"


def main(background_type, foreground_type, obstacles_type, level_type, player):
    run = True
    clock = pygame.time.Clock()
    game_speed = 16
    background_speed = 16
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0 and points < 3000:
            game_speed += 1
        if points % 250 == 0 and points < 1400:
            background_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()

        text_color = foreground(foreground_type)  # Получаем цвет текста
        text = font.render("Points: " + str(points), True, text_color)
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0
    x4_pos_bg = 0
    x5_pos_bg = 0
    x6_pos_bg = 0
    x7_pos_bg = 0
    x8_pos_bg = 0
    x9_pos_bg = 0
    x10_pos_bg = 0 
    x11_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        # Отображение фона
        if background_type == BackgroundType.DEFAULT:
            SCREEN.blit(CLASSIC1, (x1_pos_bg, 515))
            SCREEN.blit(CLASSIC1, (CLASSIC1.get_width() + x1_pos_bg, 515))

            SCREEN.blit(CLASSIC2, (x2_pos_bg, 0))
            SCREEN.blit(CLASSIC2, (CLASSIC2.get_width() + x2_pos_bg, 0))

        if background_type == BackgroundType.WINTER:
            SCREEN.blit(WINTER1, (x3_pos_bg, 555))
            SCREEN.blit(WINTER1, (WINTER1.get_width() + x3_pos_bg, 555))

            SCREEN.blit(WINTER2, (x4_pos_bg, 523))
            SCREEN.blit(WINTER2, (WINTER2.get_width() + x4_pos_bg, 523))

            SCREEN.blit(WINTER3, (x5_pos_bg, 0))
            SCREEN.blit(WINTER3, (WINTER3.get_width() + x5_pos_bg, 0))

        if background_type == BackgroundType.BEACH:
            SCREEN.blit(BEACH1, (x6_pos_bg, 510))
            SCREEN.blit(BEACH1, (BEACH1.get_width() + x6_pos_bg, 510))

            SCREEN.blit(BEACH2, (x7_pos_bg, 332))
            SCREEN.blit(BEACH2, (BEACH2.get_width() + x7_pos_bg, 332))

            SCREEN.blit(BEACH3, (x8_pos_bg, 0))
            SCREEN.blit(BEACH3, (BEACH3.get_width() + x8_pos_bg, 0))

        if background_type == BackgroundType.ZOMBI:
            SCREEN.blit(ZOMBI1, (x9_pos_bg, 550))
            SCREEN.blit(ZOMBI1, (ZOMBI1.get_width() + x9_pos_bg, 550))

            SCREEN.blit(ZOMBI2, (x10_pos_bg, 510))
            SCREEN.blit(ZOMBI2, (ZOMBI1.get_width() + x10_pos_bg, 510))

            SCREEN.blit(ZOMBI3, (x11_pos_bg, 0))
            SCREEN.blit(ZOMBI3, (ZOMBI3.get_width() + x11_pos_bg, 0))

        if len(obstacles) == 0:
            obstacle_type_random = random.randint(0, 2)
            if obstacles_type == ObstaclesType.DEFAULT and obstacle_type_random == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacles_type == ObstaclesType.DEFAULT and obstacle_type_random == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacles_type == ObstaclesType.DEFAULT and obstacle_type_random == 2:
                obstacles.append(Bird(BIRD))

            if obstacles_type == ObstaclesType.WINTER and obstacle_type_random == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS_WINTER))
            elif obstacles_type == ObstaclesType.WINTER and obstacle_type_random == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS_WINTER))
            elif obstacles_type == ObstaclesType.WINTER and obstacle_type_random == 2:
                obstacles.append(Bird(BIRD_WINTER))

            if obstacles_type == ObstaclesType.BEACH and obstacle_type_random == 0:
                obstacles.append(LargeCactus(LARGE_TREES))
            elif obstacles_type == ObstaclesType.BEACH and obstacle_type_random == 1:
                obstacles.append(LargeCactus(LARGE_BOARDS))
            elif obstacles_type == ObstaclesType.BEACH and obstacle_type_random == 2:
                obstacles.append(Bird(BIRD_BEACH))

            if obstacles_type == ObstaclesType.ZOMBI and obstacle_type_random == 0:
                obstacles.append(LargeCactus(ZOMBI))
            elif obstacles_type == ObstaclesType.ZOMBI and obstacle_type_random == 1:
                obstacles.append(LargeCactus(LARGE_GRAVES))
            elif obstacles_type == ObstaclesType.ZOMBI and obstacle_type_random == 2:
                obstacles.append(Bird(BAT))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles, game_speed)

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 60, player.dino_rect.height - 40)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 20, obstacle.rect.height - 15)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = level(level_type)
                loose_menu(death_count, level_state, points, player)
                run = False

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= game_speed
        if x1_pos_bg <= -CLASSIC1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= (background_speed - 13)
        if x2_pos_bg <= -CLASSIC2.get_width():
            x2_pos_bg = 0

        x3_pos_bg -= (background_speed + 6)
        if x3_pos_bg <= -WINTER1.get_width():
            x3_pos_bg = 0

        x4_pos_bg -= game_speed
        if x4_pos_bg <= -WINTER2.get_width():
            x4_pos_bg = 0

        x5_pos_bg -= (background_speed - 11)
        if x5_pos_bg <= -WINTER3.get_width():
           x5_pos_bg = 0

        x6_pos_bg -= game_speed
        if x6_pos_bg <= -BEACH1.get_width():
            x6_pos_bg = 0

        x7_pos_bg -= (background_speed - 10)
        if x7_pos_bg <= -BEACH2.get_width():
            x7_pos_bg = 0

        x8_pos_bg -= (background_speed - 11)
        if x8_pos_bg <= -BEACH3.get_width():
           x8_pos_bg = 0  

        x9_pos_bg -= (background_speed + 4)
        if x9_pos_bg <= -ZOMBI1.get_width():
            x9_pos_bg = 0

        x10_pos_bg -= game_speed
        if x10_pos_bg <= -ZOMBI2.get_width():
            x10_pos_bg = 0

        x11_pos_bg -= (background_speed - 10)
        if x11_pos_bg <= -ZOMBI3.get_width():
            x11_pos_bg = 0   

        pygame.display.flip()

        clock.tick(30)


def main_winter(player):
    main(BackgroundType.WINTER, ForegroundType.BLACK, ObstaclesType.WINTER, LevelType.WINTER, player)

def main_beach(player):
    main(BackgroundType.BEACH, ForegroundType.BLACK, ObstaclesType.BEACH, LevelType.BEACH, player)

def main_zombi(player):
    main(BackgroundType.ZOMBI, ForegroundType.WHITE, ObstaclesType.ZOMBI, LevelType.ZOMBI, player)


def start_menu(death_count, player, level_state):
    start_button = Button(400, 250, START)
    multiplayer_button = Button(400, 350, MULTIPLAYER)
    settings_button =Button(20, 20, SETTINGS)
    paint_button =Button(20, 120, PAINT)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(MENU, (0, 0))

        slider1_button_clicked = [False]
        slider2_button_clicked = [False]
        if death_count == 0:
            if start_button.draw() and classic_level(slider1_button_clicked, slider2_button_clicked, player, level_state):
                break
            if multiplayer_button.draw():
                pass
            if settings_button.draw():
                pass
            if paint_button.draw():
                closet(death_count, player, level_state)

        #SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 350))
        pygame.display.flip()


def loose_menu(death_count, level_state, points, player):
    pygame.mixer.music.play(-1) # Начать проигрывание музыки при возвращении в меню
    reset_button = Button(SCREEN_WIDTH // 2 - 150, 250, RESET)
    menu_button = Button(SCREEN_WIDTH // 2 - 150, 360, MENUB)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(MENU, (0, 0))

        font = pygame.font.Font('freesansbold.ttf', 45)

        if death_count > 0:
            if reset_button.draw():
                if level_state == "main":
                    main(BackgroundType.DEFAULT, ForegroundType.WHITE, ObstaclesType.DEFAULT, LevelType.DEFAULT, player)
                if level_state == "main_winter":
                    main(BackgroundType.WINTER, ForegroundType.BLACK, ObstaclesType.WINTER, LevelType.WINTER, player)
                if level_state == "main_beach":
                    main(BackgroundType.BEACH, ForegroundType.BLACK, ObstaclesType.BEACH, LevelType.BEACH, player)
                if level_state == "main_zombi":
                    main(BackgroundType.ZOMBI, ForegroundType.WHITE, ObstaclesType.ZOMBI, LevelType.ZOMBI, player)
            elif menu_button.draw():
                start_menu(death_count=0, player=Dinosaur(), level_state=None)
            score = font.render("Your Score: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(score, scoreRect)

        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 350))
        pygame.display.flip()


def classic_level(slider1_button_clicked, slider2_button_clicked, player, level_state):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(930, 563, START_LEVEL)
    #level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 330, CLASSICLEVEL)
    run = True
    level_state = "main"

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENULEVELS, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0, player=Dinosaur(), level_state=None)

        SCREEN.blit(CLASSICLEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320))

        if level_button.draw():
            main(BackgroundType.DEFAULT, ForegroundType.WHITE, ObstaclesType.DEFAULT, player)

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            winter_level(slider1_button_clicked, slider2_button_clicked, player, level_state)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            pass
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        pygame.display.flip()


def winter_level(slider1_button_clicked, slider2_button_clicked, player, level_state):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, WINTERLEVEL)
    run = True
    level_state = "main_winter"

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENULEVELS, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0, player=Dinosaur(), level_state=None)

        if level_button.draw():
            main_winter(player)

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            classic_level(slider1_button_clicked, slider2_button_clicked, player, level_state)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            beach_level(slider1_button_clicked, slider2_button_clicked, player, level_state)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        pygame.display.flip()


def beach_level(slider1_button_clicked, slider2_button_clicked, player, level_state):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, BEACHLEVEL)
    run = True
    level_state = "main_beach"

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENULEVELS, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0, player=Dinosaur(), level_state=None)

        if level_button.draw():
            main_beach(player)

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            winter_level(slider1_button_clicked, slider2_button_clicked, player, level_state)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            zombi_level(slider1_button_clicked, slider2_button_clicked, player, level_state)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False
        
        pygame.display.flip()


def zombi_level(slider1_button_clicked, slider2_button_clicked, player, level_state):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, ZOMBILEVEL)
    run = True
    level_state = "main_zombi"

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENULEVELS, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0, player=Dinosaur(), level_state=None)

        if level_button.draw():
            main_zombi(player)

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            beach_level(slider1_button_clicked, slider2_button_clicked, player, level_state)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw():
            pass

        pygame.display.flip()


def closet(death_count, player, level_state):
    SkinButton1 = Button(220, 200, SKINBUTTON1)
    SkinButton2 = Button(300, 200, SKINBUTTON2)
    SkinButton3 = Button(380, 200, SKINBUTTON3)
    SkinButton4 = Button(460, 200, SKINBUTTON3)
    SkinButton5 = Button(540, 200, SKINBUTTON3)

    SantaHat = Button(220, 300, SANTAHAT)
    Circle = Button(300, 300, CIRCLE)
    Skeleton = Button(380, 300, SKELETON)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1410, 30, OKAY)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SantaHat.draw()
        Circle.draw()
        Skeleton.draw()
                
        if SkinButton1.draw():
            death_count, level_state, player = skin1(death_count, player, level_state)
            
        if SkinButton2.draw():
            death_count, level_state, player = skin2(death_count, player, level_state)

        if SkinButton3.draw():
            pass

        if SkinButton4.draw():
            pass

        if SkinButton5.draw():
            pass

        if level_button.draw():
            start_menu(death_count, player, level_state=None)

        pygame.display.flip()


def skin1(death_count, player, level_state):
    SkinButton1 = Button(220, 200, SKINBUTTON1)
    SkinButton2 = Button(300, 200, SKINBUTTON2)
    SkinButton3 = Button(380, 200, SKINBUTTON3)
    SkinButton4 = Button(460, 200, SKINBUTTON3)
    SkinButton5 = Button(540, 200, SKINBUTTON3)

    SantaHat = Button(220, 300, SANTAHAT)
    Circle = Button(300, 300, CIRCLE)
    Skeleton = Button(380, 300, SKELETON)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1410, 30, OKAY)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if SkinButton1.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(DINOSKIN1, (940, 200))
            player = Dinosaur()

        if SantaHat.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINSANTA1, (940, 183))
            player = DinosaurWinter()

        if Circle.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINBEACH1, (940, 192))
            player = DinosaurBeach()

        if Skeleton.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINZOMBI1, (940, 200))
            player = DinosaurZombi()

        if SkinButton2.draw():
            death_count, level_state, player = skin2(death_count, player, level_state)

        if SkinButton3.draw():
            pass

        if SkinButton4.draw():
            pass

        if SkinButton5.draw():
            pass

        if level_button.draw():
            start_menu(death_count, player, level_state=None)

        pygame.display.flip()


def skin2(death_count, player, level_state):
    SkinButton1 = Button(220, 200, SKINBUTTON1)
    SkinButton2 = Button(300, 200, SKINBUTTON2)
    SkinButton3 = Button(380, 200, SKINBUTTON3)
    SkinButton4 = Button(460, 200, SKINBUTTON3)
    SkinButton5 = Button(540, 200, SKINBUTTON3)

    SantaHat = Button(220, 300, SANTAHAT)
    Circle = Button(300, 300, CIRCLE)
    Skeleton = Button(380, 300, SKELETON)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1410, 30, OKAY)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if SkinButton1.draw():
            death_count, level_state, player = skin1(death_count, player, level_state)

        if SantaHat.draw():
            pass

        if Circle.draw():
            pass

        if Skeleton.draw():
            pass

        if SkinButton2.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(DINOSKIN2, (910, 210))
            player = DinosaurSkin1()

        if SkinButton3.draw():
            pass

        if SkinButton4.draw():
            pass

        if SkinButton5.draw():
            pass

        if level_button.draw():
            start_menu(death_count, player, level_state=None)

        pygame.display.flip()

    
start_menu(death_count=0, player=Dinosaur(), level_state=None)
