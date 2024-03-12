import pygame
import os
import random

pygame.init()
pygame.mixer.init()

# Загрузка звуковых файлов
DEATH_SOUND = pygame.mixer.Sound(os.path.join("Assets/Sounds", "death_sound.wav"))
SCORE_SOUND = pygame.mixer.Sound(os.path.join("Assets/Sounds", "score_sound.wav"))
JUMP_SOUND = pygame.mixer.Sound(os.path.join("Assets/Sounds", "jump_sound.wav"))

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Adventure")

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DINOMENU = pygame.image.load(os.path.join("Assets/Dino", "DinoMenu.png"))

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

RESET = pygame.image.load(os.path.join("Assets/Other", "Reset.png"))
START = pygame.image.load(os.path.join("Assets/Other", "Start.png"))
MENUB = pygame.image.load(os.path.join("Assets/Other", "MenuB.png"))
LEVELS = pygame.image.load (os.path.join("Assets/Other", "Levels.png"))
BACK = pygame.image.load (os.path.join("Assets/Other", "Back.png"))
SLIDER1 = pygame.image.load (os.path.join("Assets/Other", "Slider1.png"))
SLIDER2 = pygame.image.load (os.path.join("Assets/Other", "Slider2.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
MENU = pygame.image.load(os.path.join("Assets/Other", "Menu.png"))

CLASSICLEVEL = pygame.image.load (os.path.join("Assets/Other", "ClassicLevel.png"))
CLASSICLEVEL2 = pygame.image.load (os.path.join("Assets/Other", "ClassicLevel2.png"))
CLASSICLEVEL3 = pygame.image.load (os.path.join("Assets/Other", "ClassicLevel3.png"))
CLASSICLEVEL4 = pygame.image.load (os.path.join("Assets/Other", "ClassicLevel4.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            JUMP_SOUND.play()  # Воспроизведение звука при прыжке
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
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


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 260
        self.index = 0

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
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 1000 == 0:
            SCORE_SOUND.play()  # Воспроизведение звука при достижении 1000 очков

        text = font.render("Points: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
            dino_rect_adjusted = pygame.Rect(player.dino_rect.x + 25, player.dino_rect.y + 15,
                                              player.dino_rect.width - 50, player.dino_rect.height - 15)
            obstacle_rect_adjusted = pygame.Rect(obstacle.rect.x + 5, obstacle.rect.y + 5,
                                                  obstacle.rect.width - 10, obstacle.rect.height - 5)

            if dino_rect_adjusted.colliderect(obstacle_rect_adjusted):
                DEATH_SOUND.play()  # Воспроизведение звука
                pygame.time.delay(2000)
                death_count += 1
                loose_menu(death_count)
                run = False

        cloud.draw(SCREEN)
        cloud.update()

        score()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


def start_menu(death_count):
    start_button = Button(SCREEN_WIDTH // 2 - 140, 200, START)
    levels_button = Button(SCREEN_WIDTH // 2 - 140, 290, LEVELS)
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(MENU, (0, 0))

        if death_count == 0:
            if start_button.draw():
                main()
            if levels_button.draw():
                levels()

        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 95, SCREEN_HEIGHT // 2 - 270))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def loose_menu(death_count):
    global points
    reset_button = Button(SCREEN_WIDTH // 2 - 140, 270, RESET)
    menu_button = Button(SCREEN_WIDTH // 2 - 140, 360, MENUB)
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(MENU, (0, 0))

        font = pygame.font.Font('freesansbold.ttf', 40)

        if death_count > 0:
            if reset_button.draw():
                main()
            elif menu_button.draw():
                start_menu(death_count=0)
            score = font.render("Your Score: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 75)
            SCREEN.blit(score, scoreRect)
        SCREEN.blit(DINOMENU, (SCREEN_WIDTH // 2 - 95, SCREEN_HEIGHT // 2 - 270))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def levels():
    back_button = Button(30, 30, BACK)
    slider1_button = Button(30, SCREEN_HEIGHT // 2 - 45, SLIDER1)
    slider2_button = Button(990, SCREEN_HEIGHT // 2 - 45, SLIDER2)
    run = True
    classic_level = True
    classic_level2 = False
    classic_level3 = False
    classic_level4 = False
    SCREEN.blit(MENU, (0, 0))

    while run:

        if back_button.draw():
            start_menu(death_count=0)

        if classic_level:
            SCREEN.blit(CLASSICLEVEL, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
            if slider1_button.draw():
                pass
            if slider2_button.draw():
                SCREEN.blit(CLASSICLEVEL2, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
                classic_level = False
                classic_level2 = True

        elif classic_level2:
            if slider1_button.draw():
                SCREEN.blit(CLASSICLEVEL, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
                classic_level = True
                classic_level2 = False
            elif slider2_button.draw():
                SCREEN.blit(CLASSICLEVEL3, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
                classic_level2 = False
                classic_level3 = True

        elif classic_level3:
            if slider1_button.draw():
                SCREEN.blit(CLASSICLEVEL2, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
                classic_level2 = True
                classic_level3 = False
            elif slider2_button.draw():
                SCREEN.blit(CLASSICLEVEL4, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
                classic_level3 = False
                classic_level4 = True

        elif classic_level4:
            if slider1_button.draw():
                SCREEN.blit(CLASSICLEVEL3, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200))
                classic_level3 = True
                classic_level4 = False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


start_menu(death_count=0)
