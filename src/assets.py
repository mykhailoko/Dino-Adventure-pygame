import pygame
import os

pygame.init()
pygame.mixer.init()

# Загрузка звуковых файлов
DEATH_SOUND = pygame.mixer.Sound(os.path.join("Assets/Sounds", "death_sound.wav"))
SCORE_SOUND = pygame.mixer.Sound(os.path.join("Assets/Sounds", "score_sound.wav"))
JUMP_SOUND = pygame.mixer.Sound(os.path.join("Assets/Sounds", "jump_sound.wav"))
MAIN_MENU_MUSIC = os.path.join("Assets/Sounds", "main_menu.mp3")

RUNNING = []
for i in range(1, 3):
    RUNNING.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRun{i}.png")))
DUCKING = []
for i in range(1, 3):
    DUCKING.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuck{i}.png"))) 
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

RUNNING_WINTER = []
for i in range(1, 3):
    RUNNING_WINTER.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRunWinter{i}.png")))
DUCKING_WINTER = []
for i in range(1, 3):
    DUCKING_WINTER.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuckWinter{i}.png"))) 
JUMPING_WINTER = pygame.image.load(os.path.join("Assets/Dino", "DinoJumpWinter.png"))

RUNNING_BEACH = []
for i in range(1, 3):
    RUNNING_BEACH.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRunBeach{i}.png")))
DUCKING_BEACH = []
for i in range(1, 3):
    DUCKING_BEACH.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuckBeach{i}.png"))) 
JUMPING_BEACH = pygame.image.load(os.path.join("Assets/Dino", "DinoJumpBeach.png"))

JUMPING_ZOMBI = pygame.image.load(os.path.join("Assets/Dino", "DinoJumpZombi.png"))

DINOMENU = pygame.image.load(os.path.join("Assets/Dino", "DinoMenu.png"))

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

SMALL_CACTUS_WINTER = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactusWinter1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactusWinter2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactusWinter3.png"))]
LARGE_CACTUS_WINTER = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactusWinter1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactusWinter2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactusWinter3.png"))]

SMALL_GRAVES = [pygame.image.load(os.path.join("Assets/Cactus", "SmallGraves1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallGraves2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallGraves3.png"))]

LARGE_GRAVES = [pygame.image.load(os.path.join("Assets/Cactus", "LargeGraves1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeGraves2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeGraves3.png"))]

LARGE_BOARDS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeBoard1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeBoard2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeBoard3.png"))]

LARGE_TREES = [pygame.image.load(os.path.join("Assets/Cactus", "LargeTree1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeTree2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeTree3.png"))]

ZOMBI = []
for i in range(1, 3):
    ZOMBI.append(pygame.image.load(os.path.join("Assets/Cactus", f"Zombi{i}.png")))

BIRD = []
for i in range(1, 3):
    BIRD.append(pygame.image.load(os.path.join("Assets/Bird", f"Bird{i}.png")))

BIRD_WINTER = []
for i in range(1, 3):
    BIRD_WINTER.append(pygame.image.load(os.path.join("Assets/Bird", f"BirdWinter{i}.png")))

BIRD_BEACH = []
for i in range(1, 3):
    BIRD_BEACH.append(pygame.image.load(os.path.join("Assets/Bird", f"BirdBeach{i}.png")))

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

RESET = pygame.image.load(os.path.join("Assets/Other", "Reset.png"))
START = pygame.image.load(os.path.join("Assets/Other", "Start.png"))
START_LEVEL = pygame.image.load(os.path.join("Assets/Other", "Start_level.png"))
MENUB = pygame.image.load(os.path.join("Assets/Other", "MenuB.png"))
LEVELS = pygame.image.load (os.path.join("Assets/Other", "Levels.png"))
BACK = pygame.image.load (os.path.join("Assets/Other", "Back.png"))
SLIDER1 = pygame.image.load (os.path.join("Assets/Other", "Slider1.png"))
SLIDER2 = pygame.image.load (os.path.join("Assets/Other", "Slider2.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
BGWINTER = pygame.image.load(os.path.join("Assets/Other", "TrackWinter.png"))
BGBEACH = pygame.image.load(os.path.join("Assets/Other", "TrackBeach.png"))
BGZOMBI = pygame.image.load(os.path.join("Assets/Other", "TrackZombi.png"))
MENU = pygame.image.load(os.path.join("Assets/Other", "Menu.png"))

CLASSICLEVEL = pygame.image.load (os.path.join("Assets/Other", "ClassicLevel.png"))
WINTERLEVEL = pygame.image.load (os.path.join("Assets/Other", "WinterLevel.png"))
BEACHLEVEL = pygame.image.load (os.path.join("Assets/Other", "BeachLevel.png"))
ZOMBILEVEL = pygame.image.load (os.path.join("Assets/Other", "ZombiLevel.png"))
