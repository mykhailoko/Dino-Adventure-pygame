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
DUCKING = []
for i in range(1, 3):
    RUNNING.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRun{i}.png")).convert_alpha())
    DUCKING.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuck{i}.png")).convert_alpha())
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png")).convert_alpha()

RUNNING_WINTER = []
DUCKING_WINTER = []
for i in range(1, 3):
    RUNNING_WINTER.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRunWinter{i}.png")).convert_alpha())
    DUCKING_WINTER.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuckWinter{i}.png")).convert_alpha()) 
JUMPING_WINTER = pygame.image.load(os.path.join("Assets/Dino", "DinoJumpWinter.png")).convert_alpha()

RUNNING_BEACH = []
DUCKING_BEACH = []
for i in range(1, 3):
    RUNNING_BEACH.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRunBeach{i}.png")).convert_alpha())
    DUCKING_BEACH.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuckBeach{i}.png")).convert_alpha()) 
JUMPING_BEACH = pygame.image.load(os.path.join("Assets/Dino", "DinoJumpBeach.png")).convert_alpha()

RUNNING_ZOMBI = []
DUCKING_ZOMBI = []
for i in range(1, 3):
    RUNNING_ZOMBI.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoRunZombi{i}.png")).convert_alpha())
    DUCKING_ZOMBI.append(pygame.image.load(os.path.join("Assets/Dino", f"DinoDuckZombi{i}.png")).convert_alpha()) 
JUMPING_ZOMBI = pygame.image.load(os.path.join("Assets/Dino", "DinoJumpZombi.png")).convert_alpha()


DINOMENU = pygame.image.load(os.path.join("Assets/Dino", "DinoMenu.png")).convert_alpha()

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png")).convert_alpha()]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png")).convert_alpha()]

SMALL_CACTUS_WINTER = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactusWinter1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactusWinter2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactusWinter3.png")).convert_alpha()]
LARGE_CACTUS_WINTER = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactusWinter1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactusWinter2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactusWinter3.png")).convert_alpha()]

SMALL_GRAVES = [pygame.image.load(os.path.join("Assets/Cactus", "SmallGraves1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallGraves2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallGraves3.png")).convert_alpha()]

LARGE_GRAVES = [pygame.image.load(os.path.join("Assets/Cactus", "LargeGraves1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeGraves2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeGraves3.png")).convert_alpha()]

LARGE_BOARDS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeBoard1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeBoard2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeBoard3.png")).convert_alpha()]

LARGE_TREES = [pygame.image.load(os.path.join("Assets/Cactus", "LargeTree1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeTree2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeTree3.png")).convert_alpha()]

ZOMBI = []
for i in range(1, 3):
    ZOMBI.append(pygame.image.load(os.path.join("Assets/Cactus", f"Zombi{i}.png")).convert_alpha())

BIRD = []
for i in range(1, 3):
    BIRD.append(pygame.image.load(os.path.join("Assets/Bird", f"Bird{i}.png")).convert_alpha())

BIRD_WINTER = []
for i in range(1, 3):
    BIRD_WINTER.append(pygame.image.load(os.path.join("Assets/Bird", f"BirdWinter{i}.png")).convert_alpha())

BIRD_BEACH = []
for i in range(1, 3):
    BIRD_BEACH.append(pygame.image.load(os.path.join("Assets/Bird", f"BirdBeach{i}.png")).convert_alpha())

BAT = []
for i in range(1, 3):
    BAT.append(pygame.image.load(os.path.join("Assets/Bird", f"Bat{i}.png")).convert_alpha())

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png")).convert_alpha()

RESET = pygame.image.load(os.path.join("Assets/Other", "Reset.png")).convert_alpha()
START = pygame.image.load(os.path.join("Assets/Other", "Start.png")).convert_alpha()
START_LEVEL = pygame.image.load(os.path.join("Assets/Other", "Start_level.png")).convert_alpha()
MENUB = pygame.image.load(os.path.join("Assets/Other", "MenuB.png")).convert_alpha()
LEVELS = pygame.image.load (os.path.join("Assets/Other", "Levels.png")).convert_alpha()
BACK = pygame.image.load (os.path.join("Assets/Other", "Back.png")).convert_alpha()
SLIDER1 = pygame.image.load (os.path.join("Assets/Other", "Slider1.png")).convert_alpha()
SLIDER2 = pygame.image.load (os.path.join("Assets/Other", "Slider2.png")).convert_alpha()

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png")).convert_alpha()
BGWINTER = pygame.image.load(os.path.join("Assets/Other", "TrackWinter.png")).convert_alpha()
BGBEACH = pygame.image.load(os.path.join("Assets/Other", "TrackBeach.png")).convert_alpha()
BGZOMBI = pygame.image.load(os.path.join("Assets/Other", "TrackZombi.png")).convert_alpha()
BEACH1 = pygame.image.load(os.path.join("Assets/Other", "Beach1.png")).convert_alpha()
BEACH2 = pygame.image.load(os.path.join("Assets/Other", "Beach2.png")).convert_alpha()
BEACH3 = pygame.image.load(os.path.join("Assets/Other", "Beach3.png")).convert_alpha()
ZOMBI1 = pygame.image.load(os.path.join("Assets/Other", "Zombi1.png")).convert_alpha()
ZOMBI2 = pygame.image.load(os.path.join("Assets/Other", "Zombi2.png")).convert_alpha()
ZOMBI3 = pygame.image.load(os.path.join("Assets/Other", "Zombi3.png")).convert_alpha()
CLASSIC1 = pygame.image.load(os.path.join("Assets/Other", "Classic1.png")).convert_alpha()
CLASSIC2 = pygame.image.load(os.path.join("Assets/Other", "Classic2.png")).convert_alpha()
WINTER1 = pygame.image.load(os.path.join("Assets/Other", "Winter1.png")).convert_alpha()
WINTER2 = pygame.image.load(os.path.join("Assets/Other", "Winter2.png")).convert_alpha()
WINTER3 = pygame.image.load(os.path.join("Assets/Other", "Winter3.png")).convert_alpha()
MENU = pygame.image.load(os.path.join("Assets/Other", "Menu.png")).convert_alpha()

CLASSICLEVEL = pygame.image.load (os.path.join("Assets/Other", "ClassicLevel.png")).convert_alpha()
WINTERLEVEL = pygame.image.load (os.path.join("Assets/Other", "WinterLevel.png")).convert_alpha()
BEACHLEVEL = pygame.image.load (os.path.join("Assets/Other", "BeachLevel.png")).convert_alpha()
ZOMBILEVEL = pygame.image.load (os.path.join("Assets/Other", "ZombiLevel.png")).convert_alpha()
