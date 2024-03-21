import pygame
import os
import random
from assets import *
from dinosaur import *

pygame.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERES'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 3, screen_height - 60

SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width
#SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
SCREEN = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Dino Adventure")

pygame.mixer.music.load(MAIN_MENU_MUSIC)
pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость музыки (от 0 до 1)
pygame.mixer.music.play(-1)  # -1 означает,что музыка будет воспроизводиться в цикле бесконечно 

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= background_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Zombi(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 410
        self.index = 0

    def update(self):
        self.rect.x -= (game_speed - 2)
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 435


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 410


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 310
        self.index = 0

    def update(self):
        self.rect.x -= (game_speed + 5)
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1


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
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, level_state, background_speed, run_level, run
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 16
    background_speed = 6 
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 23)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop() # Остановить проигрывание музыки при запуске игры     

    def score():
        global points, game_speed, background_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 200 == 0 and points < 1400:
            background_speed += 1
        if points > 1600:
            background_speed == background_speed
        if points % 1000 == 0:
            SCORE_SOUND.play()  # Воспроизведение звука при достижении 1000 очков

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= background_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        background()

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 50, player.dino_rect.height - 35)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 10)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()  # Воспроизведение звука
                pygame.time.delay(700)
                death_count += 1
                level_state = "main"
                loose_menu(death_count)
                run = False

        cloud.draw(SCREEN)
        cloud.update()

        score()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


def main_winter():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, level_state, background_speed, run_level, run
    run = True
    clock = pygame.time.Clock()
    player = DinosaurWinter()
    game_speed = 16
    background_speed = 6 
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop() # Остановить проигрывание музыки при запуске игры     

    def score():
        global points, game_speed, background_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 200 == 0 and points < 1400:
            background_speed += 1
        if points > 1600:
            background_speed == background_speed
        if points % 1000 == 0:
            SCORE_SOUND.play()  # Воспроизведение звука при достижении 1000 очков

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BGWINTER.get_width()
        SCREEN.blit(BGWINTER, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BGWINTER, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BGWINTER, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= background_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        background()

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS_WINTER))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS_WINTER))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD_WINTER))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 50, player.dino_rect.height - 35)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 10)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()  # Воспроизведение звука
                pygame.time.delay(700)
                death_count += 1
                level_state = "main_winter"
                loose_menu(death_count)
                run = False
                run_level = False

        score()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


def main_beach():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, level_state, background_speed, run_level, run
    run = True
    clock = pygame.time.Clock()
    player = DinosaurBeach()
    game_speed = 16
    background_speed = 6 
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop() # Остановить проигрывание музыки при запуске игры     

    def score():
        global points, game_speed, background_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 200 == 0 and points < 1400:
            background_speed += 1
        if points > 1600:
            background_speed == background_speed
        if points % 1000 == 0:
            SCORE_SOUND.play()  # Воспроизведение звука при достижении 1000 очков

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BGBEACH.get_width()
        SCREEN.blit(BGBEACH, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BGBEACH, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BGBEACH, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= background_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        background()

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(LargeCactus(LARGE_TREES))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_BOARDS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD_BEACH))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 50, player.dino_rect.height - 35)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 10)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()  # Воспроизведение звука
                pygame.time.delay(700)
                death_count += 1
                level_state = "main_beach"
                loose_menu(death_count)
                run = False
                run_level = False

        score()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


def main_zombi():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, level_state, background_speed, run_level, run
    run = True
    clock = pygame.time.Clock()
    player = DinosaurZombi()
    game_speed = 16
    background_speed = 6
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    pygame.mixer.music.stop() # Остановить проигрывание музыки при запуске игры     

    def score():
        global points, game_speed, background_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 200 == 0 and points < 1400:
            background_speed += 1
        if points > 1600:
            background_speed == background_speed
        if points % 1000 == 0:
            SCORE_SOUND.play()  # Воспроизведение звука при достижении 1000 очков

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1440, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BGZOMBI.get_width()
        SCREEN.blit(BGZOMBI, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BGZOMBI, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BGZOMBI, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= background_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        userInput = pygame.key.get_pressed()

        SCREEN.fill((255, 255, 255))

        background()

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Zombi(ZOMBI))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_GRAVES))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()

            # Столкновение
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x, player.dino_rect.y,
                                              player.dino_rect.width - 50, player.dino_rect.height - 35)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x, obstacle.rect.y,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 10)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()  # Воспроизведение звука
                pygame.time.delay(700)
                death_count += 1
                level_state = "main_zombi"
                loose_menu(death_count)
                run = False
                run_level = False

        score()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


def start_menu(death_count):
    global run_level, run
    start_button = Button(SCREEN_WIDTH // 2 - 150, 250, START)
    levels_button = Button(SCREEN_WIDTH // 2 - 150, 360, LEVELS)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(MENU, (0, 0))

        if death_count == 0:
            if start_button.draw():
                main()
            if levels_button.draw():
                classic_level()

        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 400))
        pygame.display.update()


def loose_menu(death_count):
    global points, level_state, run_level, run
    pygame.mixer.music.play(-1) # Начать проигрывание музыки при возвращении в меню
    reset_button = Button(SCREEN_WIDTH // 2 - 150, 250, RESET)
    menu_button = Button(SCREEN_WIDTH // 2 - 150, 360, MENUB)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

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
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
            SCREEN.blit(score, scoreRect)
        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 400))
        pygame.display.update()


slider1_button_clicked = False
slider2_button_clicked = False
classic_level_button_clicked = False

def classic_level():
    global slider1_button_clicked, slider2_button_clicked, run_level, run
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 70, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 70, SLIDER2)
    level_button = Button(930, 590, START_LEVEL)
    run_level = True

    SCREEN.blit(MENU, (0, 0))

    while run_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        if back_button.draw():
            start_menu(death_count=0)

        SCREEN.blit(CLASSICLEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 330))

        if level_button.draw():
            main()

        if slider2_button.draw() and not slider2_button_clicked:
            slider2_button_clicked = True
            winter_level()
        elif not slider2_button.draw():
            slider2_button_clicked = False

        if slider1_button.draw():
            pass

        if slider2_button.draw() and not slider2_button_clicked:
            slider2_button_clicked = True
            winter_level()
        elif not slider2_button.draw():
            slider2_button_clicked = False

        pygame.display.update()


def winter_level():
    global slider1_button_clicked, slider2_button_clicked, run_level, run
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 70, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 70, SLIDER2)
    level_button = Button(930, 590, START_LEVEL)
    run_level = True

    SCREEN.blit(MENU, (0, 0))

    while run_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        if back_button.draw():
            start_menu(death_count=0)

        SCREEN.blit(WINTERLEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 330))

        if level_button.draw():
            main_winter()

        if slider1_button.draw() and not slider1_button_clicked:
            slider1_button_clicked = True
            classic_level()
        elif not slider1_button.draw():
            slider1_button_clicked = False

        if slider2_button.draw() and not slider2_button_clicked:
            slider2_button_clicked = True
            beach_level()
        elif not slider2_button.draw():
            slider2_button_clicked = False

        pygame.display.update()

  
def beach_level():
    global slider1_button_clicked, slider2_button_clicked, run_level, run
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 70, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 70, SLIDER2)
    level_button = Button(930, 590, START_LEVEL)
    run_level = True

    SCREEN.blit(MENU, (0, 0))

    while run_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        if back_button.draw():
            start_menu(death_count=0)

        SCREEN.blit(BEACHLEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 330))

        if level_button.draw():
            main_beach()

        if slider1_button.draw() and not slider1_button_clicked:
            slider1_button_clicked = True
            winter_level()
        elif not slider1_button.draw():
            slider1_button_clicked = False

        if slider2_button.draw() and not slider2_button_clicked:
            slider2_button_clicked = True
            zombi_level()
        elif not slider2_button.draw():
            slider2_button_clicked = False
        
        pygame.display.update()


def zombi_level():
    global slider1_button_clicked, slider2_button_clicked, run_level, run
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 70, SLIDER1)
    slider2_button = Button(1410, SCREEN_HEIGHT // 2 - 70, SLIDER2)
    level_button = Button(930, 590, START_LEVEL)
    run_level = True

    SCREEN.blit(MENU, (0, 0))

    while run_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_level = False

        if back_button.draw():
            start_menu(death_count=0)

        SCREEN.blit(ZOMBILEVEL, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 330))

        if level_button.draw():
            main_zombi()

        if slider1_button.draw() and not slider1_button_clicked:
            slider1_button_clicked = True
            beach_level()
        elif not slider1_button.draw():
            slider1_button_clicked = False

        if slider2_button.draw():
            pass

        pygame.display.update()

    
start_menu(death_count=0)
