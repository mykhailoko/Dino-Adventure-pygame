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


def main(player, level_state):
    run = True
    clock = pygame.time.Clock()
    game_speed = 17
    background_speed = 17
    points = 0 

    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    boosts = []
    death_count = 0
    main_music_playing = False

    pause_button = Button(1465, 30, PAUSE)
    paused = False

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
        if points % 500 == 0 and points < 3000:
            game_speed += 1
        if points % 500 == 0 and points < 1400:
            background_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (80, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed
    
    def pause_board(death_count, player, paused, level_state, points):
            pause_start = Button(620, 330, PAUSERESUME)
            pause_menu = Button(620, 440, PAUSEMENU)
            
            SCREEN.blit(PAUSEBOARD, (420, 170))

            if pause_start.draw():
                paused = False

            if pause_menu.draw():
                death_count += 1
                level_state = "main"
                loose_menu(death_count, level_state, points, player)
                stop_music()

            return paused

    x1_pos_bg = 0
    x2_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Нажата кнопка 'p' (пауза)
                    paused = not paused  # Изменить состояние паузы 
            
        if paused == False:
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

            if pause_button.draw():
                paused = True

            points, game_speed, background_speed = score(points, game_speed, background_speed)

            player.draw(SCREEN)
            player.update(userInput)

            x1_pos_bg -= game_speed
            if x1_pos_bg <= -CLASSIC1.get_width():
                x1_pos_bg = 0

            x2_pos_bg -= (background_speed - 14)
            if x2_pos_bg <= -CLASSIC2.get_width():
                x2_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)

        if paused == True:
            paused = pause_board(death_count, player, paused, level_state, points)

    play_menu_music()


def main_winter(player, level_state):
    run = True
    clock = pygame.time.Clock()
    game_speed = 17
    background_speed = 17
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    winter_music_playing = False
    pause_button = Button(1465, 30, PAUSE)
    paused = False

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
        textRect.center = (80, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed
    
    def pause_board(death_count, player, paused, level_state, points):
            pause_start = Button(620, 330, PAUSERESUME)
            pause_menu = Button(620, 440, PAUSEMENU)
            
            SCREEN.blit(PAUSEBOARD, (420, 170))

            if pause_start.draw():
                paused = False

            if pause_menu.draw():
                death_count += 1
                level_state = "main_winter"
                loose_menu(death_count, level_state, points, player)
                stop_music()

            return paused

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Нажата кнопка 'p' (пауза)
                    paused = not paused  # Изменить состояние паузы 
            
        if paused == False:
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

            if pause_button.draw():
                paused = True       

            points, game_speed, background_speed = score(points, game_speed, background_speed)

            player.draw(SCREEN)
            player.update(userInput)

            x1_pos_bg -= (background_speed + 3)
            if x1_pos_bg <= -WINTER1.get_width():
                x1_pos_bg = 0

            x2_pos_bg -= game_speed 
            if x2_pos_bg <= -WINTER2.get_width():
                x2_pos_bg = 0

            x3_pos_bg -= (background_speed - 15)
            if x3_pos_bg <= -WINTER3.get_width():
                x3_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)

        if paused == True:
            paused = pause_board(death_count, player, paused, level_state, points)

    # После выхода из цикла уровня, вызов функции воспроизведения музыки из меню
    play_menu_music()


def main_beach(player, level_state):
    run = True
    clock = pygame.time.Clock()
    game_speed = 17
    background_speed = 17
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    beach_music_playing = False

    pause_button = Button(1465, 30, PAUSE)
    paused = False

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
        textRect.center = (80, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed
    
    def pause_board(death_count, player, paused, level_state, points):
            pause_start = Button(620, 330, PAUSERESUME)
            pause_menu = Button(620, 440, PAUSEMENU)
            
            SCREEN.blit(PAUSEBOARD, (420, 170))

            if pause_start.draw():
                paused = False

            if pause_menu.draw():
                death_count += 1
                level_state = "main_beach"
                loose_menu(death_count, level_state, points, player)
                stop_music()

            return paused

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Нажата кнопка 'p' (пауза)
                    paused = not paused  # Изменить состояние паузы 
            
        if paused == False:
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

            if pause_button.draw():
                paused = True  

            points, game_speed, background_speed = score(points, game_speed, background_speed)

            player.draw(SCREEN)
            player.update(userInput)

            x1_pos_bg -= game_speed
            if x1_pos_bg <= -BEACH1.get_width():
                x1_pos_bg = 0

            x2_pos_bg -= (background_speed - 12)
            if x2_pos_bg <= -BEACH2.get_width():
                x2_pos_bg = 0

            x3_pos_bg -= (background_speed - 13)
            if x3_pos_bg <= -BEACH3.get_width():
                x3_pos_bg = 0

        pygame.display.flip()    

        clock.tick(30)

        if paused == True:
            paused = pause_board(death_count, player, paused, level_state, points)

    play_menu_music()


def main_zombi(player, level_state):
    run = True
    clock = pygame.time.Clock()
    game_speed = 16
    background_speed = 16
    points = 0 
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    zombi_music_playing = False

    pause_button = Button(1465, 30, PAUSEWHITE)
    paused = False

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
        textRect.center = (80, 40)
        SCREEN.blit(text, textRect)
        return points, game_speed, background_speed

    def pause_board(death_count, player, paused, level_state, points):
            pause_start = Button(620, 330, PAUSERESUME)
            pause_menu = Button(620, 440, PAUSEMENU)
            
            SCREEN.blit(PAUSEBOARD, (420, 170))

            if pause_start.draw():
                paused = False

            if pause_menu.draw():
                death_count += 1
                level_state = "main_zombi"
                loose_menu(death_count, level_state, points, player)
                stop_music()

            return paused

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Нажата кнопка 'p' (пауза)
                    paused = not paused  # Изменить состояние паузы 
            
        if paused == False:
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

            if pause_button.draw():
                paused = True  

            points, game_speed, background_speed = score(points, game_speed, background_speed)

            player.draw(SCREEN)
            player.update(userInput)

            x1_pos_bg -= (background_speed + 2)
            if x1_pos_bg <= -ZOMBI1.get_width():
                x1_pos_bg = 0

            x2_pos_bg -= game_speed
            if x2_pos_bg <= -ZOMBI2.get_width():
                x2_pos_bg = 0

            x3_pos_bg -= (background_speed - 14)
            if x3_pos_bg <= -ZOMBI3.get_width():
                x3_pos_bg = 0

        pygame.display.flip()

        clock.tick(30)

        if paused == True:
            paused = pause_board(death_count, player, paused, level_state, points)

    play_menu_music()


def start_menu(player, death_count, level_state):
    start_button = Button(400, 230, START)
    multiplayer_button = Button(400, 330, MULTIPLAYER)
    settings_button = Button(5, 5, SETTINGS)
    paint_button = Button(5, 99, PAINT)
    exit = Button(1465, 15, EXIT)
    start_clicked = False
    mult_clicked = False
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
            if start_button.draw() and not start_clicked:
                start_clicked = True
                SCREEN.blit(MENU, (0, 0))
                SCREEN.blit(START_CLICK, (409, 234)) 
                multiplayer_button.draw()
                settings_button.draw()
                paint_button.draw()
                exit.draw()
                pygame.display.flip() 
                pygame.time.delay(700)
                classic_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
            elif not start_button.draw():
                start_clicked = False

            if multiplayer_button.draw() and not mult_clicked:
                mult_clicked = True
                SCREEN.blit(MENU, (0, 0))
                SCREEN.blit(MULT_CLICK, (409, 334))
                start_button.draw()
                settings_button.draw()
                paint_button.draw()
                exit.draw()
                pygame.display.flip()
                pygame.time.delay(700)
                multiplayer(player, level_state, 3, 3)
            elif not multiplayer_button.draw():
                mult_clicked = False

            if settings_button.draw():
                pass
            if paint_button.draw():
                closet(player, death_count, level_state)
            if exit.draw():
                exit_board(death_count, player, level_state)

        pygame.display.flip()

        
def exit_board(death_count, player, level_state):
    exit_yes = Button(610, 430, EXITYES)
    exit_no = Button(800, 430, EXITNO)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.blit(EXITMENU, (0, 0))
        SCREEN.blit(EXITBOARD, (400, 170))
        if exit_yes.draw():
            quit()
        if exit_no.draw():
            start_menu(player, death_count, level_state)

        pygame.display.flip()


def loose_menu(death_count, level_state, points, player):
    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)
    play_menu_music()
    reset_button = Button(940, 280, RESET)
    menu_button = Button(940, 390, MENUB)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(LOOSEMENU, (0, 0))

        font = pygame.font.Font('freesansbold.ttf', 55)

        if death_count > 0:
            if reset_button.draw():
                if level_state == "main":
                    main(player, level_state)
                if level_state == "main_winter":
                    main_winter(player, level_state)
                if level_state == "main_beach":
                    main_beach(player, level_state)
                if level_state == "main_zombi":
                    main_zombi(player, level_state)

            if menu_button.draw():
                start_menu(player, death_count=0, level_state=None)
            score = font.render("Your Score: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (470, 130)
            SCREEN.blit(score, scoreRect)

            if points < 1000:
                SCREEN.blit(MESSAGE1, (490, 230))
            if points > 1000 and points < 4000:
                SCREEN.blit(MESSAGE2, (490, 230))
            if points > 4000:
                SCREEN.blit(MESSAGE3, (490, 230))
            SCREEN.blit(DINOSKIN1, (100, 250))

        pygame.display.flip()


def classic_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state):
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 60, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 60, SLIDER2)
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
            start_menu(player, death_count=0, level_state=None)

        SCREEN.blit(CLASSICLEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 320))

        if level_button.draw() and not level_button_clicked[0]:
            level_button_clicked[0] = True
            main(player, level_state)
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
            start_menu(player, death_count=0, level_state=None)

        if level_button.draw():
            main_winter(player, level_state)

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
            start_menu(player, death_count=0, level_state=None)

        if level_button.draw():
            main_beach(player, level_state)

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
            start_menu(player, death_count=0, level_state=None)

        if level_button.draw():
            main_zombi(player, level_state)

        if slider1_button.draw() and not slider1_button_clicked[0]:
            slider1_button_clicked[0] = True
            beach_level(slider1_button_clicked, slider2_button_clicked, level_button_clicked, player, level_state)
        elif not slider1_button.draw():
            slider1_button_clicked[0] = False

        if slider2_button.draw():
            pass

        pygame.display.flip()


def closet(player, death_count, level_state):
    SkinButton1 = Button(290, 200, SKINBUTTON1)
    SkinButton2 = Button(380, 200, SKINBUTTON2)
    SkinButton3 = Button(470, 200, SKINBUTTON3)

    SantaHat = Button(290, 300, SANTAHAT)
    Circle = Button(380, 300, CIRCLE)
    Skeleton = Button(470, 300, SKELETON)
    Cowboy = Button(290, 390, COWBOY)
    Viking = Button(380, 390, VIKING)
    Clown = Button(470, 390, CLOWN)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1385, 50, OKAY)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SantaHat.draw()
        Circle.draw()
        Skeleton.draw()
        Cowboy.draw()
        Viking.draw()
        Clown.draw()
                
        if SkinButton1.draw():
            player, death_count, level_state = skin1(player, death_count, level_state)
            
        if SkinButton2.draw():
            player, death_count, level_state = skin2(player, death_count, level_state)

        if SkinButton3.draw():
            player, death_count, level_state = skin3(player, death_count, level_state)

        if level_button.draw():
            start_menu(player, death_count=0, level_state=None)

        pygame.display.flip()


def skin1(player, death_count, level_state):
    SkinButton1 = Button(290, 200, SKINBUTTON1)
    SkinButton2 = Button(380, 200, SKINBUTTON2)
    SkinButton3 = Button(470, 200, SKINBUTTON3)

    SantaHat = Button(290, 300, SANTAHAT)
    Circle = Button(380, 300, CIRCLE)
    Skeleton = Button(470, 300, SKELETON)
    Cowboy = Button(290, 390, COWBOY)
    Viking = Button(380, 390, VIKING)
    Clown = Button(470, 390, CLOWN)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1385, 50, OKAY)

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
            SCREEN.blit(SKINZOMBI1, (941, 201))
            player = DinosaurZombi()

        if Cowboy.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINCOWBOY1, (940, 166))
            player = DinosaurCowboy()

        if Viking.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINVIKING1, (940, 128))
            player = DinosaurViking()

        if Clown.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINCLOWN1, (940, 172))
            player = DinosaurClown()

        if SkinButton2.draw():
            player, death_count, level_state = skin2(player, death_count, level_state)

        if SkinButton3.draw():
            player, death_count, level_state = skin3(player, death_count, level_state)

        if level_button.draw():
            start_menu(player, death_count=0, level_state=None)

        pygame.display.flip()


def skin2(player, death_count, level_state):
    SkinButton1 = Button(290, 200, SKINBUTTON1)
    SkinButton2 = Button(380, 200, SKINBUTTON2)
    SkinButton3 = Button(470, 200, SKINBUTTON3)

    SantaHat = Button(290, 300, SANTAHAT)
    Circle = Button(380, 300, CIRCLE)
    Skeleton = Button(470, 300, SKELETON)
    Cowboy = Button(290, 390, COWBOY)
    Viking = Button(380, 390, VIKING)
    Clown = Button(470, 390, CLOWN)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1385, 50, OKAY)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if SkinButton1.draw():
            player, death_count, level_state = skin1(player, death_count, level_state)

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

        if Cowboy.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINCOWBOY2, (910, 184))
            player = DinosaurSkin1Cowboy()

        if Viking.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINVIKING2, (910, 142))
            player = DinosaurSkin1Viking()
        
        if Clown.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINCLOWN2, (910, 176))
            player = DinosaurSkin1Clown()

        if SkinButton2.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(DINOSKIN2, (910, 210))
            player = DinosaurSkin1()

        if SkinButton3.draw():
            player, death_count, level_state = skin3(player, death_count, level_state)

        if level_button.draw():
            start_menu(player, death_count=0, level_state=None)

        pygame.display.flip()

def skin3(player, death_count, level_state):
    SkinButton1 = Button(290, 200, SKINBUTTON1)
    SkinButton2 = Button(380, 200, SKINBUTTON2)
    SkinButton3 = Button(470, 200, SKINBUTTON3)

    SantaHat = Button(290, 300, SANTAHAT)
    Circle = Button(380, 300, CIRCLE)
    Skeleton = Button(470, 300, SKELETON)
    Cowboy = Button(290, 390, COWBOY)
    Viking = Button(380, 390, VIKING)
    Clown = Button(470, 390, CLOWN)

    run = True

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(CLOSET, (0, 0))

    level_button = Button(1385, 50, OKAY)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if SkinButton1.draw():
            player, death_count, level_state = skin1(player, death_count, level_state)

        if SantaHat.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINSANTA3, (910, 180))
            player = DinosaurSkin3Winter() 

        if Circle.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINBEACH3, (910, 200))
            player = DinosaurSkin3Beach()

        if Skeleton.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINZOMBI3, (910, 200))
            player = DinosaurSkin3Zombi()

        if Cowboy.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINCOWBOY3, (910, 171))
            player = DinosaurSkin3Cowboy()

        if Viking.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINVIKING3, (910, 130))
            player = DinosaurSkin3Viking()

        if Clown.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(SKINCLOWN3, (910, 174))
            player = DinosaurSkin3Clown()

        if SkinButton2.draw():
            player, death_count, level_state = skin2(player, death_count, level_state)

        if SkinButton3.draw():
            SCREEN.blit(CLOSET, (0, 0))
            SCREEN.blit(DINOSKIN3, (910, 200))
            player = DinosaurSkin3()

        if level_button.draw():
            start_menu(player, death_count=0, level_state=None)

        pygame.display.flip()


def multiplayer(player, level_state, heart1, heart2):
    run = True
    clock = pygame.time.Clock()
    game_speed = 18
    background_speed = 18
    player1 = DinosaurMultiplayer1()
    player2 = DinosaurMultiplayer2()

    obstacles1 = []
    obstacles2 = []
    death_count = 0
    main_music_playing = False

    pause_button = Button(1465, 30, PAUSE)
    paused = False

    def play_main_music():
        pygame.mixer.music.load(MAIN_LEVEL_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def pause_board(death_count, player, paused, level_state):
            pause_start = Button(620, 330, PAUSERESUME)
            pause_menu = Button(620, 440, PAUSEMENU)
            
            SCREEN.blit(PAUSEBOARD, (420, 170))

            if pause_start.draw():
                paused = False

            if pause_menu.draw():
                death_count += 1
                level_state = "multiplayer"
                multiplayer_loose_menu(death_count, level_state, player, heart1, heart2)
                stop_music()

            return paused
    
    # Проверяем, не проигрывается ли уже музыка
    if not main_music_playing:
        play_main_music()
        main_music_playing = True

    x1_pos_bg = 0
    x2_pos_bg = 0
    x3_pos_bg = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Нажата кнопка 'p' (пауза)
                    paused = not paused  # Изменить состояние паузы 
            
        if paused == False:
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

            SCREEN.blit(MULTARROWS, (130, 17))
            SCREEN.blit(MULTWS, (130, 430))

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
                
                if heart1 == 3:
                    SCREEN.blit(PLAYER1, (10, 18))
                    SCREEN.blit(HEART, (10, 50))
                    SCREEN.blit(HEART, (45, 50))
                    SCREEN.blit(HEART, (80, 50))
                
                if heart1 == 2:
                    SCREEN.blit(PLAYER1, (10, 18))
                    SCREEN.blit(HEART, (10, 50))
                    SCREEN.blit(HEART, (45, 50))

                if heart1 == 1:
                    SCREEN.blit(PLAYER1, (10, 18))
                    SCREEN.blit(HEART, (10, 50))

                if dino_rect_adjusted.colliderect(obstacle1_rect_adjusted) and heart1 != 0:
                    DEATH_SOUND.play()
                    pygame.time.delay(700)
                    heart1 = heart1 - 1
                    obstacles1 = []
                    obstacles2 = []

                if dino_rect_adjusted.colliderect(obstacle1_rect_adjusted) and heart1 == 0:
                    DEATH_SOUND.play()
                    pygame.time.delay(700)
                    death_count += 1
                    level_state = "multiplayer"
                    multiplayer_loose_menu(death_count, level_state, player, heart1, heart2)
                    run = False


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
                
                if heart2 == 3:
                    SCREEN.blit(PLAYER2, (10, 430))
                    SCREEN.blit(HEART, (10, 461))
                    SCREEN.blit(HEART, (45, 461))
                    SCREEN.blit(HEART, (80, 461))
                
                if heart2 == 2:
                    SCREEN.blit(PLAYER2, (10, 430))
                    SCREEN.blit(HEART, (10, 461))
                    SCREEN.blit(HEART, (45, 461))

                if heart2 == 1:
                    SCREEN.blit(PLAYER2, (10, 430))
                    SCREEN.blit(HEART, (10, 461))

                if dino_rect_adjusted.colliderect(obstacle2_rect_adjusted) and heart2 != 0:
                    DEATH_SOUND.play()
                    pygame.time.delay(700)
                    heart2 = heart2 - 1
                    obstacles1 = []
                    obstacles2 = []

                if dino_rect_adjusted.colliderect(obstacle2_rect_adjusted) and heart2 == 0:
                    DEATH_SOUND.play()
                    pygame.time.delay(700)
                    death_count += 1
                    level_state = "multiplayer"
                    multiplayer_loose_menu(death_count, level_state, player, heart1, heart2)
                    run = False

            if pause_button.draw():
                paused = True

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

        if paused == True:
            paused = pause_board(death_count, player, paused, level_state)


def multiplayer_loose_menu(death_count, level_state, player, heart1, heart2):
    def play_menu_music():
        pygame.mixer.music.load(MAIN_MENU_MUSIC)
        pygame.mixer.music.play(-1)
    play_menu_music()
    reset_button = Button(1000, 300, RESET)
    menu_button = Button(1000, 410, MENUB)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(MULTIPLAYERLOOSE, (0, 0))

        if death_count > 0:
            if reset_button.draw():
                if level_state == "multiplayer":
                    multiplayer(player, level_state, heart1=3, heart2=3)

            if menu_button.draw():
                start_menu(death_count=0, player=Dinosaur(), level_state=None)

        if heart1 > heart2:
            SCREEN.blit(DINOSKIN1, (270, 230))

        if heart2 > heart1:
            SCREEN.blit(DINOSKIN2, (240, 230))

        if heart1 == heart2:
            pass

        pygame.display.flip()

    
start_menu(player=Dinosaur(), death_count=0, level_state=None)
