import pygame
import os
import random                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

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


def main(player):
    run = True
    clock = pygame.time.Clock()
    game_speed = 16
    background_speed = 16
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    main_music_playing = False

    def play_main_music():
        pygame.mixer.music.load(MAIN_LEVEL_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 200 == 0 and points < 3000:
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

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not main_music_playing:
            play_main_music()
            main_music_playing = True

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
                                              player.dino_rect.width - 60, player.dino_rect.height - 40)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 20, obstacle.rect.height - 15)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = "main"
                loose_menu(death_count, level_state, points, player)
                run = False
                stop_music()

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= game_speed
        if x1_pos_bg <= -CLASSIC1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= (background_speed - 13)
        if x2_pos_bg <= -CLASSIC2.get_width():
            x2_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)

    play_menu_music()


def main_winter(player):
    run = True
    clock = pygame.time.Clock()
    game_speed = 16
    background_speed = 16
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    winter_music_playing = False

    def play_winter_music():
        pygame.mixer.music.load(WINTER_LEVEL_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0 and points < 3000:
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

        if not winter_music_playing:
            play_winter_music()
            winter_music_playing = True

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        SCREEN.blit(WINTER1, (x1_pos_bg, 555))
        SCREEN.blit(WINTER1, (WINTER1.get_width() + x1_pos_bg, 555))

        SCREEN.blit(WINTER2, (x2_pos_bg, 523))
        SCREEN.blit(WINTER2, (WINTER2.get_width() + x2_pos_bg, 523))

        SCREEN.blit(WINTER3, (x3_pos_bg, 0))
        SCREEN.blit(WINTER3, (WINTER3.get_width() + x3_pos_bg, 0))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SNOWMAN))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(SKIS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD_WINTER))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles, game_speed)

            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 60, player.dino_rect.height - 40)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 20, obstacle.rect.height - 15)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = "main_winter"
                loose_menu(death_count, level_state, points, player)
                run = False
                stop_music()
                

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player.draw(SCREEN)
        player.update(userInput)

        x1_pos_bg -= (background_speed + 3)
        if x1_pos_bg <= -WINTER1.get_width():
            x1_pos_bg = 0

        x2_pos_bg -= game_speed 
        if x2_pos_bg <= -WINTER2.get_width():
            x2_pos_bg = 0

        x3_pos_bg -= (background_speed - 13)
        if x3_pos_bg <= -WINTER3.get_width():
            x3_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)

    # После выхода из цикла уровня, вызов функции воспроизведения музыки из меню
    play_menu_music()


def main_beach(player):
    run = True
    clock = pygame.time.Clock()
    game_speed = 16
    background_speed = 16
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    beach_music_playing = False

    def play_beach_music():
        pygame.mixer.music.load(BEACH_LEVEL_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0 and points < 3000:
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

        if not beach_music_playing:
            play_beach_music()
            beach_music_playing = True
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
                loose_menu(death_count, level_state, points, player)
                run = False
                stop_music()

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
    play_menu_music()


def main_zombi(player):
    run = True
    clock = pygame.time.Clock()
    game_speed = 16
    background_speed = 16
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    zombi_music_playing = False

    def play_zombi_music():
        pygame.mixer.music.load(ZOMBI_LEVEL_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0 and points < 3000:
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

        if not zombi_music_playing:
            play_zombi_music()
            zombi_music_playing = True
            
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
                loose_menu(death_count, level_state, points, player)
                run = False
                stop_music()

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

    play_menu_music()


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
        level_button_clicked = [False]
        if death_count == 0:
            if start_button.draw() and not level_button_clicked[0]:
                level_button_clicked[0] = True
                if classic_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state):
                    break 
            elif not start_button.draw():
                level_button_clicked[0] = False
            if multiplayer_button.draw():
                multiplayer(player)
            if settings_button.draw():
                pass
            if paint_button.draw():
                closet(death_count, player, level_state)

        #SCREEN.blit(EXITMENU, (0, 0))
        #SCREEN.blit(EXIT, (1450, 30))
        #SCREEN.blit(EXITBOARD, (400, 170))
        #SCREEN.blit(EXITYES, (610, 430))
        #SCREEN.blit(EXITNO, (800, 430))

        pygame.display.flip()


def loose_menu(death_count, level_state, points, player):
    #pygame.mixer.music.play(-1) # Начать проигрывание музыки при возвращении в меню
    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)
    play_menu_music()
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
                    main(player)
                if level_state == "main_winter":
                    main_winter(player)
                if level_state == "main_beach":
                    main_beach(player)
                if level_state == "main_zombi":
                    main_zombi(player)
                if level_state == "multiplayer":
                    multiplayer(player)
            elif menu_button.draw():
                start_menu(death_count=0, player=Dinosaur(), level_state=None)
            score = font.render("Your Score: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(score, scoreRect)

        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 350))
        pygame.display.flip()


def classic_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
    #level_button = Button(930, 563, START_LEVEL)
    level_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320, CLASSICLEVEL)
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

        if level_button.draw() and not level_button_clicked[0]:
            level_button_clicked[0] = True
            main(player)
        elif not level_button.draw():
            level_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            winter_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            pass
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        pygame.display.flip()


def winter_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state):
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
            classic_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            beach_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        pygame.display.flip()


def beach_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state):
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
            winter_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw() and not slider2_button_clicked[0]:
            slider2_button_clicked[0] = True
            zombi_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
        elif not slider2_button.draw():
            slider2_button_clicked[0] = False

        pygame.display.flip()



def zombi_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state):
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
            beach_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
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
            SCREEN.blit(SKINZOMBI1, (940, 201))
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
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINSANTA2, (910, 197))
            player = DinosaurSkin1Winter()

        if Circle.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINBEACH2, (910, 210))
            player = DinosaurSkin1Beach()

        if Skeleton.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINZOMBI2, (910, 210))
            player = DinosaurSkin1Zombi()

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


def multiplayer(player):
    run = True
    clock = pygame.time.Clock()
    game_speed = 14
    background_speed = 16
    points = 0 
    player1 = DinosaurMultiplayer1()
    player2 = DinosaurMultiplayer2()

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles1 = []
    obstacles2 = []
    death_count = 0
    main_music_playing = False

    def play_main_music():
        pygame.mixer.music.load(MAIN_LEVEL_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def score(points, game_speed, background_speed):
        points += 1
        if points % 100 == 0 and points < 1500:
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

        if not main_music_playing:
            play_main_music()
            main_music_playing = True

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        # Отображение фона
        SCREEN.blit(MULTIPLAYERBG1, (x1_pos_bg, 0))
        SCREEN.blit(MULTIPLAYERBG1, (MULTIPLAYERBG1.get_width() + x1_pos_bg, 0))

        SCREEN.blit(MULTIPLAYERBG1, (x1_pos_bg, 413))
        SCREEN.blit(MULTIPLAYERBG1, (MULTIPLAYERBG1.get_width() + x1_pos_bg, 413))

        SCREEN.blit(MULTIPLAYERBG2, (x2_pos_bg, 299))
        SCREEN.blit(MULTIPLAYERBG2, (MULTIPLAYERBG2.get_width() + x2_pos_bg, 299))

        SCREEN.blit(MULTIPLAYERBG2, (x2_pos_bg, 712))
        SCREEN.blit(MULTIPLAYERBG2, (MULTIPLAYERBG2.get_width() + x2_pos_bg, 712))

        SCREEN.blit(MULTIPLAYERBG3, (x3_pos_bg, 397))
        SCREEN.blit(MULTIPLAYERBG3, (MULTIPLAYERBG3.get_width() + x3_pos_bg, 397))


        if len(obstacles1) == 0:
            obstacle_type1 = random.randint(0, 2)
            if obstacle_type1 == 0:
                obstacles1.append(SmallCactusMultiplayer1(SMALL_CACTUS))
            elif obstacle_type1 == 1:
                obstacles1.append(LargeCactusMultiplayer1(LARGE_CACTUS))
            elif obstacle_type1 == 2:
                obstacles1.append(BirdMultiplayer1(BIRD))

        for obstacle1 in obstacles1:
            obstacle1.draw(SCREEN)
            obstacle1.update(obstacles1, game_speed)
 
            # Столкновение
            dino_rect_adjusted = pygame.Rect(player1.dino_rect.x, player1.dino_rect.y,
                                              player1.dino_rect.width - 60, player1.dino_rect.height - 40)
            obstacle1_rect_adjusted = pygame.Rect(obstacle1.rect.x, obstacle1.rect.y,
                                                  obstacle1.rect.width - 20, obstacle1.rect.height - 15)
            
            if dino_rect_adjusted.colliderect(obstacle1_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = "multiplayer"
                loose_menu(death_count, level_state, points, player)
                run = False
                stop_music()
            

        if len(obstacles2) == 0:
            obstacle_type2 = random.randint(0, 2)
            if obstacle_type2 == 0:
                obstacles2.append(SmallCactusMultiplayer2(SMALL_CACTUS))
            elif obstacle_type2 == 1:
                obstacles2.append(LargeCactusMultiplayer2(LARGE_CACTUS))
            elif obstacle_type2 == 2:
                obstacles2.append(BirdMultiplayer2(BIRD))

        for obstacle2 in obstacles2:
            obstacle2.draw(SCREEN)
            obstacle2.update(obstacles2, game_speed)
 
            # Столкновение
            dino_rect_adjusted = pygame.Rect(player2.dino_rect.x, player2.dino_rect.y,
                                              player2.dino_rect.width - 60, player2.dino_rect.height - 40)
            obstacle2_rect_adjusted = pygame.Rect(obstacle2.rect.x, obstacle2.rect.y,
                                                  obstacle2.rect.width - 20, obstacle2.rect.height - 15)

            if dino_rect_adjusted.colliderect(obstacle2_rect_adjusted):
                DEATH_SOUND.play()
                pygame.time.delay(700)
                death_count += 1
                level_state = "multiplayer"
                loose_menu(death_count, level_state, points, player)
                run = False
                stop_music()

        points, game_speed, background_speed = score(points, game_speed, background_speed)

        player1.draw(SCREEN)
        player1.update(userInput)

        player2.draw(SCREEN)
        player2.update(userInput)

        x2_pos_bg -= game_speed
        if x2_pos_bg <= -MULTIPLAYERBG2.get_width():
            x2_pos_bg = 0

        x1_pos_bg -= (background_speed - 14)
        if x1_pos_bg <= -MULTIPLAYERBG1.get_width():
            x1_pos_bg = 0

        x3_pos_bg -= (background_speed - 14)
        if x3_pos_bg <= -MULTIPLAYERBG3.get_width():
            x3_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)
    
start_menu(death_count=0, player=Dinosaur(), level_state=None)
