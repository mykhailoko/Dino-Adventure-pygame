import pygame
import os
import random

pygame.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERES'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 3, screen_height - 60

SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width
SCREEN = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Dino Adventure")

from assets import *
from dinosaur import *
from obstacles import *

pygame.mixer.music.load(MAIN_MENU_MUSIC)
pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость музыки (от 0 до 1)
pygame.mixer.music.play(-1)  # -1 означает,что музыка будет воспроизводиться в цикле бесконечно 
    
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return action

  
def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 16
    background_speed = 16
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 250 == 0 and points < 1400:
            background_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed

    x1_pos_bg = 0
    x2_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        # Отображение фона
        SCREEN.blit(CLASSIC1, (x1_pos_bg, 515))
        SCREEN.blit(CLASSIC1, (CLASSIC1.get_width() + x1_pos_bg, 515))

        SCREEN.blit(CLASSIC2, (x2_pos_bg, 0))
        SCREEN.blit(CLASSIC2, (CLASSIC2.get_width() + x2_pos_bg, 0))

        if len(obstacles) == 0:
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_type == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_type == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles, game_speed)

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 50, player.dino_rect.height - 35)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 10)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = "main"
                loose_menu(death_count, level_state, points)
                run = False

        cloud.draw(SCREEN)
        cloud.update(background_speed)

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= game_speed
        if x1_pos_bg <= -CLASSIC1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= (background_speed - 10)
        if x2_pos_bg <= -CLASSIC2.get_width():
            x2_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)


def main_winter():
    run = True
    clock = pygame.time.Clock()
    player = DinosaurWinter()
    game_speed = 16
    background_speed = 16
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 250 == 0 and points < 1400:
            background_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        # Отображение фона 
        SCREEN.blit(WINTER1, (x1_pos_bg, 555))
        SCREEN.blit(WINTER1, (WINTER1.get_width() + x1_pos_bg, 555))

        SCREEN.blit(WINTER2, (x2_pos_bg, 523))
        SCREEN.blit(WINTER2, (WINTER2.get_width() + x2_pos_bg, 523))

        SCREEN.blit(WINTER3, (x3_pos_bg, 0))
        SCREEN.blit(WINTER3, (WINTER3.get_width() + x3_pos_bg, 0))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS_WINTER))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS_WINTER))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD_WINTER))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles, game_speed)

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 50, player.dino_rect.height - 35)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 10)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = "main_winter"
                loose_menu(death_count, level_state, points)
                run = False

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= (background_speed + 6)
        if x1_pos_bg <= -WINTER1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= game_speed
        if x2_pos_bg <= -WINTER2.get_width():
            x2_pos_bg = 0

        x3_pos_bg -= (background_speed - 11)
        if x3_pos_bg <= -WINTER3.get_width():
           x3_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)


def main_beach():
    run = True
    clock = pygame.time.Clock()
    player = DinosaurBeach()
    game_speed = 14
    background_speed = 14
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 250 == 0 and points < 1400:
            background_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        # Отображение фона 
        SCREEN.blit(BEACH1, (x1_pos_bg, 510))
        SCREEN.blit(BEACH1, (BEACH1.get_width() + x1_pos_bg, 510))

        SCREEN.blit(BEACH2, (x2_pos_bg, 332))
        SCREEN.blit(BEACH2, (BEACH2.get_width() + x2_pos_bg, 332))

        SCREEN.blit(BEACH3, (x3_pos_bg, 0))
        SCREEN.blit(BEACH3, (BEACH3.get_width() + x3_pos_bg, 0))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(LargeCactus(LARGE_TREES))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_BOARDS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD_BEACH))

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
                level_state = "main_beach"
                loose_menu(death_count, level_state, points)
                run = False

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= game_speed
        if x1_pos_bg <= -BEACH1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= (background_speed - 10)
        if x2_pos_bg <= -BEACH2.get_width():
            x2_pos_bg = 0

        x3_pos_bg -= (background_speed - 11)
        if x3_pos_bg <= -BEACH3.get_width():
           x3_pos_bg = 0

        pygame.display.flip()    

        clock.tick(30)


def main_zombi():
    run = True
    clock = pygame.time.Clock()
    player = DinosaurZombi()
    game_speed = 14
    background_speed = 14
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 250 == 0 and points < 1400:
            background_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        # Отображение фона 
        SCREEN.blit(ZOMBI1, (x1_pos_bg, 550))
        SCREEN.blit(ZOMBI1, (ZOMBI1.get_width() + x1_pos_bg, 550))

        SCREEN.blit(ZOMBI2, (x2_pos_bg, 510))
        SCREEN.blit(ZOMBI2, (ZOMBI1.get_width() + x2_pos_bg, 510))

        SCREEN.blit(ZOMBI3, (x3_pos_bg, 0))
        SCREEN.blit(ZOMBI3, (ZOMBI3.get_width() + x3_pos_bg, 0))


        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Zombi(ZOMBI))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_GRAVES))
            elif random.randint(0, 2) == 2:
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
                level_state = "main_zombi"
                loose_menu(death_count, level_state, points)
                run = False

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= (background_speed + 4)
        if x1_pos_bg <= -ZOMBI1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= game_speed
        if x2_pos_bg <= -ZOMBI2.get_width():
            x2_pos_bg = 0

        x3_pos_bg -= (background_speed - 10)
        if x3_pos_bg <= -ZOMBI3.get_width():
            x3_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)


def start_menu(death_count):
    start_button = Button(SCREEN_WIDTH // 2 - 150, 250, START)
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
            if start_button.draw() and classic_level(slider1_button_clicked, slider2_button_clicked):
                break

        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 350))
        pygame.display.flip()


def loose_menu(death_count, level_state, points):
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
                    main()
                if level_state == "main_winter":
                    main_winter()
                if level_state == "main_beach":
                    main_beach()
                if level_state == "main_zombi":
                    main_zombi()
            elif menu_button.draw():
                start_menu(death_count=0)
            score = font.render("Your Score: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(score, scoreRect)

        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 350))
        pygame.display.flip()


def classic_level(slider1_button_clicked, slider2_button_clicked):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(930, 563, START_LEVEL)
    #level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 330, CLASSICLEVEL)
    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENU, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0)

        SCREEN.blit(CLASSICLEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320))

        if level_button.draw():
            main()

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            winter_level(slider1_button_clicked, slider2_button_clicked)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            pass
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        pygame.display.flip()


def winter_level(slider1_button_clicked, slider2_button_clicked):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, WINTERLEVEL)
    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENU, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0)

        if level_button.draw():
            main_winter()

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            classic_level(slider1_button_clicked, slider2_button_clicked)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            beach_level(slider1_button_clicked, slider2_button_clicked)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        pygame.display.flip()


def beach_level(slider1_button_clicked, slider2_button_clicked):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, BEACHLEVEL)
    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENU, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0)

        if level_button.draw():
            main_beach()

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            winter_level(slider1_button_clicked, slider2_button_clicked)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            zombi_level(slider1_button_clicked, slider2_button_clicked)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False
        
        pygame.display.flip()


def zombi_level(slider1_button_clicked, slider2_button_clicked):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, ZOMBILEVEL)
    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(MENU, (0, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if back_button.draw():
            start_menu(death_count=0)

        if level_button.draw():
            main_zombi()

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            beach_level(slider1_button_clicked, slider2_button_clicked)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw():
            pass

        pygame.display.flip()

    
start_menu(death_count=0)
