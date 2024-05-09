import pygame
import os

pygame.init()
pygame.mixer.init()

# Загрузка звуковых файлов
DEATH_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Sounds", "death_sound.wav"))
SCORE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Sounds", "score_sound.wav"))
JUMP_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Sounds", "jump_sound.wav"))
MAIN_MENU_MUSIC = os.path.join("Assets", "Sounds", "main_menu.mp3")
WINTER_LEVEL_MUSIC = os.path.join("Assets", "Sounds", "winter_level.mp3")
BEACH_LEVEL_MUSIC = os.path.join("Assets", "Sounds", "beach_level.mp3")
ZOMBI_LEVEL_MUSIC = os.path.join("Assets", "Sounds", "zombi_level.mp3")
MAIN_LEVEL_MUSIC = os.path.join("Assets", "Sounds", "main_level.mp3")

RUNNING = []
DUCKING = []
for i in range(1, 3):
    RUNNING.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRun{i}.png")).convert_alpha())
    DUCKING.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuck{i}.png")).convert_alpha())
JUMPING = pygame.image.load(os.path.join("Assets", "Dino", "DinoJump.png")).convert_alpha()

RUNNING_SKIN1 = []
DUCKING_SKIN1 = []
for i in range(1, 3):
    RUNNING_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1Run{i}.png")).convert_alpha())
    DUCKING_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1Duck{i}.png")).convert_alpha())
JUMPING_SKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1Jump.png")).convert_alpha()

RUNNING_SKIN3 = []
DUCKING_SKIN3 = []
for i in range(1, 3):
    RUNNING_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3Run{i}.png")).convert_alpha())
    DUCKING_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3Duck{i}.png")).convert_alpha())
JUMPING_SKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3Jump.png")).convert_alpha()

RUNNING_WINTER = []
DUCKING_WINTER = []
for i in range(1, 3):
    RUNNING_WINTER.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRunWinter{i}.png")).convert_alpha())
    DUCKING_WINTER.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuckWinter{i}.png")).convert_alpha()) 
JUMPING_WINTER = pygame.image.load(os.path.join("Assets", "Dino", "DinoJumpWinter.png")).convert_alpha()

RUNNING_WINTER_SKIN1 = []
DUCKING_WINTER_SKIN1 = []
for i in range(1, 3):
    RUNNING_WINTER_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1RunWinter{i}.png")).convert_alpha())
    DUCKING_WINTER_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1DuckWinter{i}.png")).convert_alpha()) 
JUMPING_WINTER_SKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1JumpWinter.png")).convert_alpha()

RUNNING_WINTER_SKIN3 = []
DUCKING_WINTER_SKIN3 = []
for i in range(1, 3):
    RUNNING_WINTER_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3RunWinter{i}.png")).convert_alpha())
    DUCKING_WINTER_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3DuckWinter{i}.png")).convert_alpha()) 
JUMPING_WINTER_SKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3JumpWinter.png")).convert_alpha()

RUNNING_BEACH = []
DUCKING_BEACH = []
for i in range(1, 3):
    RUNNING_BEACH.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRunBeach{i}.png")).convert_alpha())
    DUCKING_BEACH.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuckBeach{i}.png")).convert_alpha()) 
JUMPING_BEACH = pygame.image.load(os.path.join("Assets", "Dino", "DinoJumpBeach.png")).convert_alpha()

RUNNING_BEACH_SKIN1 = []
DUCKING_BEACH_SKIN1 = []
for i in range(1, 3):
    RUNNING_BEACH_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1RunBeach{i}.png")).convert_alpha())
    DUCKING_BEACH_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1DuckBeach{i}.png")).convert_alpha()) 
JUMPING_BEACH_SKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1JumpBeach.png")).convert_alpha()

RUNNING_BEACH_SKIN3 = []
DUCKING_BEACH_SKIN3 = []
for i in range(1, 3):
    RUNNING_BEACH_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3RunBeach{i}.png")).convert_alpha())
    DUCKING_BEACH_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3DuckBeach{i}.png")).convert_alpha()) 
JUMPING_BEACH_SKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3JumpBeach.png")).convert_alpha()

RUNNING_ZOMBI = []
DUCKING_ZOMBI = []
for i in range(1, 3):
    RUNNING_ZOMBI.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRunZombi{i}.png")).convert_alpha())
    DUCKING_ZOMBI.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuckZombi{i}.png")).convert_alpha()) 
JUMPING_ZOMBI = pygame.image.load(os.path.join("Assets", "Dino", "DinoJumpZombi.png")).convert_alpha()

RUNNING_SKIN1_ZOMBI = []
DUCKING_SKIN1_ZOMBI = []
for i in range(1, 3):
    RUNNING_SKIN1_ZOMBI.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1RunZombi{i}.png")).convert_alpha())
    DUCKING_SKIN1_ZOMBI.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1DuckZombi{i}.png")).convert_alpha()) 
JUMPING_SKIN1_ZOMBI = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1JumpZombi.png")).convert_alpha()

RUNNING_SKIN3_ZOMBI = []
DUCKING_SKIN3_ZOMBI = []
for i in range(1, 3):
    RUNNING_SKIN3_ZOMBI.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3RunZombi{i}.png")).convert_alpha())
    DUCKING_SKIN3_ZOMBI.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3DuckZombi{i}.png")).convert_alpha()) 
JUMPING_SKIN3_ZOMBI = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3JumpZombi.png")).convert_alpha()

RUNNING_COWBOY = []
DUCKING_COWBOY = []
for i in range(1, 3):
    RUNNING_COWBOY.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRunCowboy{i}.png")).convert_alpha())
    DUCKING_COWBOY.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuckCowboy{i}.png")).convert_alpha())
JUMPING_COWBOY = pygame.image.load(os.path.join("Assets", "Dino", "DinoJumpCowboy.png")).convert_alpha()

RUNNING_COWBOY_SKIN1 = []
DUCKING_COWBOY_SKIN1 = []
for i in range(1, 3):
    RUNNING_COWBOY_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1RunCowboy{i}.png")).convert_alpha())
    DUCKING_COWBOY_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1DuckCowboy{i}.png")).convert_alpha())
JUMPING_COWBOY_SKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1JumpCowboy.png")).convert_alpha()

RUNNING_COWBOY_SKIN3 = []
DUCKING_COWBOY_SKIN3 = []
for i in range(1, 3):
    RUNNING_COWBOY_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3RunCowboy{i}.png")).convert_alpha())
    DUCKING_COWBOY_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3DuckCowboy{i}.png")).convert_alpha())
JUMPING_COWBOY_SKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3JumpCowboy.png")).convert_alpha()

RUNNING_VIKING = []
DUCKING_VIKING = []
for i in range(1, 3):
    RUNNING_VIKING.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRunViking{i}.png")).convert_alpha())
    DUCKING_VIKING.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuckViking{i}.png")).convert_alpha())
JUMPING_VIKING = pygame.image.load(os.path.join("Assets", "Dino", "DinoJumpViking.png")).convert_alpha()

RUNNING_VIKING_SKIN1 = []
DUCKING_VIKING_SKIN1 = []
for i in range(1, 3):
    RUNNING_VIKING_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1RunViking{i}.png")).convert_alpha())
    DUCKING_VIKING_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1DuckViking{i}.png")).convert_alpha())
JUMPING_VIKING_SKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1JumpViking.png")).convert_alpha()

RUNNING_VIKING_SKIN3 = []
DUCKING_VIKING_SKIN3 = []
for i in range(1, 3):
    RUNNING_VIKING_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3RunViking{i}.png")).convert_alpha())
    DUCKING_VIKING_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3DuckViking{i}.png")).convert_alpha())
JUMPING_VIKING_SKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3JumpViking.png")).convert_alpha()

RUNNING_CLOWN = []
DUCKING_CLOWN = []
for i in range(1, 3):
    RUNNING_CLOWN.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoRunClown{i}.png")).convert_alpha())
    DUCKING_CLOWN.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoDuckClown{i}.png")).convert_alpha())
JUMPING_CLOWN = pygame.image.load(os.path.join("Assets", "Dino", "DinoJumpClown.png")).convert_alpha()

RUNNING_CLOWN_SKIN1 = []
DUCKING_CLOWN_SKIN1 = []
for i in range(1, 3):
    RUNNING_CLOWN_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1RunClown{i}.png")).convert_alpha())
    DUCKING_CLOWN_SKIN1.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin1DuckClown{i}.png")).convert_alpha())
JUMPING_CLOWN_SKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1JumpClown.png")).convert_alpha()

RUNNING_CLOWN_SKIN3 = []
DUCKING_CLOWN_SKIN3 = []
for i in range(1, 3):
    RUNNING_CLOWN_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3RunClown{i}.png")).convert_alpha())
    DUCKING_CLOWN_SKIN3.append(pygame.image.load(os.path.join("Assets", "Dino", f"DinoSkin3DuckClown{i}.png")).convert_alpha())
JUMPING_CLOWN_SKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3JumpClown.png")).convert_alpha()

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus3.png")).convert_alpha()]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus3.png")).convert_alpha()]


SNOWMAN = [pygame.image.load(os.path.join("Assets", "Cactus", "Snowman1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "Snowman2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "Snowman3.png")).convert_alpha()]
SKIS = [pygame.image.load(os.path.join("Assets", "Cactus", "Skis1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "Skis2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "Skis3.png")).convert_alpha()]

SMALL_GRAVES = [pygame.image.load(os.path.join("Assets", "Cactus", "SmallGraves1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "SmallGraves2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "SmallGraves3.png")).convert_alpha()]

LARGE_GRAVES = [pygame.image.load(os.path.join("Assets", "Cactus", "LargeGraves1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeGraves2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeGraves3.png")).convert_alpha()]

LARGE_BOARDS = [pygame.image.load(os.path.join("Assets", "Cactus", "LargeBoard1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeBoard2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeBoard3.png")).convert_alpha()]

LARGE_TREES = [pygame.image.load(os.path.join("Assets", "Cactus", "LargeTree1.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeTree2.png")).convert_alpha(),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeTree3.png")).convert_alpha()]

ZOMBI = []
for i in range(1, 3):
    ZOMBI.append(pygame.image.load(os.path.join("Assets", "Cactus", f"Zombi{i}.png")).convert_alpha())

BIRD = []
for i in range(1, 3):
    BIRD.append(pygame.image.load(os.path.join("Assets", "Bird", f"Bird{i}.png")).convert_alpha())

BIRD_WINTER = []
for i in range(1, 3):
    BIRD_WINTER.append(pygame.image.load(os.path.join("Assets", "Bird", f"BirdWinter{i}.png")).convert_alpha())

BIRD_BEACH = []
for i in range(1, 3):
    BIRD_BEACH.append(pygame.image.load(os.path.join("Assets", "Bird", f"BirdBeach{i}.png")).convert_alpha())

BAT = []
for i in range(1, 3):
    BAT.append(pygame.image.load(os.path.join("Assets", "Bird", f"Bat{i}.png")).convert_alpha())

CLOUD = pygame.image.load(os.path.join("Assets", "Other", "Cloud.png")).convert_alpha()

RESET = pygame.image.load(os.path.join("Assets", "Other", "Reset.png")).convert_alpha()
START = pygame.image.load(os.path.join("Assets", "Other", "Start.png")).convert_alpha()
START_LEVEL = pygame.image.load(os.path.join("Assets", "Other", "Start_level.png")).convert_alpha()
MENUB = pygame.image.load(os.path.join("Assets", "Other", "MenuB.png")).convert_alpha()
MULTIPLAYER = pygame.image.load(os.path.join("Assets", "Other", "MultButton.png")).convert_alpha()
LEVELS = pygame.image.load (os.path.join("Assets", "Other", "Levels.png")).convert_alpha()
SETTINGS = pygame.image.load (os.path.join("Assets", "Other", "Settings.png")).convert_alpha()
PAINT = pygame.image.load (os.path.join("Assets", "Other", "Paint.png")).convert_alpha()
BACK = pygame.image.load (os.path.join("Assets", "Other", "Back.png")).convert_alpha()
SLIDER1 = pygame.image.load (os.path.join("Assets", "Other", "Slider1.png")).convert_alpha()
SLIDER2 = pygame.image.load (os.path.join("Assets", "Other", "Slider2.png")).convert_alpha()

START_CLICK = pygame.image.load(os.path.join("Assets", "Other", "StartClick.png")).convert_alpha()
MULT_CLICK = pygame.image.load(os.path.join("Assets", "Other", "MultButtonClick.png")).convert_alpha()

BG = pygame.image.load(os.path.join("Assets", "Other", "Track.png")).convert_alpha()
BGWINTER = pygame.image.load(os.path.join("Assets", "Other", "TrackWinter.png")).convert_alpha()
BGBEACH = pygame.image.load(os.path.join("Assets", "Other", "TrackBeach.png")).convert_alpha()
BGZOMBI = pygame.image.load(os.path.join("Assets", "Other", "TrackZombi.png")).convert_alpha()
BEACH1 = pygame.image.load(os.path.join("Assets", "Other", "Beach1.png")).convert_alpha()
BEACH2 = pygame.image.load(os.path.join("Assets", "Other", "Beach2.png")).convert_alpha()
BEACH3 = pygame.image.load(os.path.join("Assets", "Other", "Beach3.png")).convert_alpha()
ZOMBI1 = pygame.image.load(os.path.join("Assets", "Other", "Zombi1.png")).convert_alpha()
ZOMBI2 = pygame.image.load(os.path.join("Assets", "Other", "Zombi2.png")).convert_alpha()
ZOMBI3 = pygame.image.load(os.path.join("Assets", "Other", "Zombi3.png")).convert_alpha()
CLASSIC1 = pygame.image.load(os.path.join("Assets", "Other", "Classic1.png")).convert_alpha()
CLASSIC2 = pygame.image.load(os.path.join("Assets", "Other", "Classic2.png")).convert_alpha()
WINTER1 = pygame.image.load(os.path.join("Assets", "Other", "Winter1.png")).convert_alpha()
WINTER2 = pygame.image.load(os.path.join("Assets", "Other", "Winter2.png")).convert_alpha()
WINTER3 = pygame.image.load(os.path.join("Assets", "Other", "Winter3.png")).convert_alpha()
MENU = pygame.image.load(os.path.join("Assets", "Other", "Menu.png")).convert_alpha()
LOOSEMENU = pygame.image.load(os.path.join("Assets", "Other", "LooseMenu.png")).convert_alpha()

CLASSICLEVEL = pygame.image.load (os.path.join("Assets", "Other", "ClassicLevel.png")).convert_alpha()
WINTERLEVEL = pygame.image.load (os.path.join("Assets", "Other", "WinterLevel.png")).convert_alpha()
BEACHLEVEL = pygame.image.load (os.path.join("Assets", "Other", "BeachLevel.png")).convert_alpha()
ZOMBILEVEL = pygame.image.load (os.path.join("Assets", "Other", "ZombiLevel.png")).convert_alpha()

DINOSKIN1 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin1.png")).convert_alpha()
SKINSANTA1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinSanta1.png")).convert_alpha()
SKINBEACH1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinBeach1.png")).convert_alpha()
SKINZOMBI1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinZombi1.png")).convert_alpha()
SKINCOWBOY1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinCowboy1.png")).convert_alpha()
SKINVIKING1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinViking1.png")).convert_alpha()
SKINCLOWN1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinClown1.png")).convert_alpha()

DINOSKIN2 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin2.png")).convert_alpha()
SKINSANTA2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinSanta2.png")).convert_alpha()
SKINBEACH2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinBeach2.png")).convert_alpha()
SKINZOMBI2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinZombi2.png")).convert_alpha()
SKINCOWBOY2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinCowboy2.png")).convert_alpha()
SKINVIKING2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinViking2.png")).convert_alpha()
SKINCLOWN2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinClown2.png")).convert_alpha()

DINOSKIN3 = pygame.image.load(os.path.join("Assets", "Dino", "DinoSkin3.png")).convert_alpha()
SKINSANTA3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinSanta3.png")).convert_alpha()
SKINBEACH3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinBeach3.png")).convert_alpha()
SKINZOMBI3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinZombi3.png")).convert_alpha()
SKINCOWBOY3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinCowboy3.png")).convert_alpha()
SKINVIKING3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinViking3.png")).convert_alpha()
SKINCLOWN3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinClown3.png")).convert_alpha()

SKINBUTTON1 = pygame.image.load(os.path.join("Assets", "Dino", "SkinButton1.png")).convert_alpha()
SKINBUTTON2 = pygame.image.load(os.path.join("Assets", "Dino", "SkinButton2.png")).convert_alpha()
SKINBUTTON3 = pygame.image.load(os.path.join("Assets", "Dino", "SkinButton3.png")).convert_alpha()

CLOSET = pygame.image.load (os.path.join("Assets", "Other", "Closet.png")).convert_alpha()

SANTAHAT = pygame.image.load(os.path.join("Assets", "Dino", "SantaHat.png")).convert_alpha()
CIRCLE = pygame.image.load(os.path.join("Assets", "Dino", "Circle.png")).convert_alpha()
SKELETON = pygame.image.load(os.path.join("Assets", "Dino", "Skeleton.png")).convert_alpha()
COWBOY = pygame.image.load(os.path.join("Assets", "Dino", "Cowboy.png")).convert_alpha()
VIKING = pygame.image.load(os.path.join("Assets", "Dino", "Viking.png")).convert_alpha()
CLOWN = pygame.image.load(os.path.join("Assets", "Dino", "Clown.png")).convert_alpha()

OKAY = pygame.image.load (os.path.join("Assets", "Other", "Okay.png")).convert_alpha()
MENULEVELS = pygame.image.load (os.path.join("Assets", "Other", "MenuLevels.png")).convert_alpha()

BOOST = [pygame.image.load (os.path.join("Assets", "Other", "boost.png")).convert_alpha(),
         pygame.image.load (os.path.join("Assets", "Other", "boost.png")).convert_alpha(),
         pygame.image.load (os.path.join("Assets", "Other", "boost.png")).convert_alpha()]

MULTIPLAYERBG1 = pygame.image.load (os.path.join("Assets", "Other", "multiplayer1.png")).convert_alpha()
MULTIPLAYERBG2 = pygame.image.load (os.path.join("Assets", "Other", "multiplayer2.png")).convert_alpha()
MULTIPLAYERBG3 = pygame.image.load (os.path.join("Assets", "Other", "multiplayer3.png")).convert_alpha()

EXIT = pygame.image.load (os.path.join("Assets", "Other", "Exit.png")).convert_alpha()
EXITBOARD = pygame.image.load (os.path.join("Assets", "Other", "ExitBoard.png")).convert_alpha()
EXITYES = pygame.image.load (os.path.join("Assets", "Other", "ExitYes.png")).convert_alpha()
EXITNO = pygame.image.load (os.path.join("Assets", "Other", "ExitNo.png")).convert_alpha()
EXITMENU = pygame.image.load (os.path.join("Assets", "Other", "ExitMenu.png")).convert_alpha()

DOWN = pygame.image.load (os.path.join("Assets", "Other", "down.png")).convert_alpha()
UP = pygame.image.load (os.path.join("Assets", "Other", "up.png")).convert_alpha()

HEART = pygame.image.load (os.path.join("Assets", "Other", "heart.png")).convert_alpha()
PLAYER1 = pygame.image.load (os.path.join("Assets", "Other", "Player1.png")).convert_alpha()
PLAYER2 = pygame.image.load (os.path.join("Assets", "Other", "Player2.png")).convert_alpha()

PAUSE = pygame.image.load (os.path.join("Assets", "Other", "pause.png")).convert_alpha()
PAUSEWHITE = pygame.image.load (os.path.join("Assets", "Other", "pause_white.png")).convert_alpha()
PAUSEBOARD = pygame.image.load (os.path.join("Assets", "Other", "PauseBoard.png")).convert_alpha()
PAUSERESUME = pygame.image.load (os.path.join("Assets", "Other", "Resume.png")).convert_alpha()
PAUSEMENU = pygame.image.load (os.path.join("Assets", "Other", "MenuB.png")).convert_alpha()

MULTIPLAYERLOOSE = pygame.image.load (os.path.join("Assets", "Other", "MultiplayerLoose.png")).convert_alpha()
MULTARROWS = pygame.image.load (os.path.join("Assets", "Other", "MultArrows.png")).convert_alpha()
MULTWS = pygame.image.load (os.path.join("Assets", "Other", "MultWS.png")).convert_alpha()

MESSAGE1 = pygame.image.load (os.path.join("Assets", "Other", "Message1.png")).convert_alpha()
MESSAGE2 = pygame.image.load (os.path.join("Assets", "Other", "Message2.png")).convert_alpha()
MESSAGE3 = pygame.image.load (os.path.join("Assets", "Other", "Message3.png")).convert_alpha()