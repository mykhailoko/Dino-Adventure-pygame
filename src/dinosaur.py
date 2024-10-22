from assets import *
from button import *

class Dinosaur:
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 460
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

        '''
        # android version
        down = Button(200, 620, DOWN)
        up = Button(1200, 620, UP)

        if up.draw() and not self.dino_jump:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True 
        if down.draw() and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        '''

        if self.dino_duck:
            self.duck()
        elif self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0 

        if userInput[pygame.K_UP] and not self.dino_jump:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_SPACE] and not self.dino_jump:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_w] and not self.dino_jump:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif userInput[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif userInput[pygame.K_LCTRL] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif userInput[pygame.K_RCTRL] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN] or userInput[pygame.K_s]):
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
            if self.dino_rect.y >= self.Y_POS:  # Условие, чтобы динозавр не уходил под землю
                self.dino_rect.y = self.Y_POS
                self.jump_vel = self.JUMP_VEL
                self.dino_jump = False


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class DinosaurWinter(Dinosaur):
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 455
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_WINTER
        self.run_img = RUNNING_WINTER
        self.jump_img = JUMPING_WINTER

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurBeach(Dinosaur):
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 455
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_BEACH
        self.run_img = RUNNING_BEACH
        self.jump_img = JUMPING_BEACH

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurZombi(Dinosaur):
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 450
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_ZOMBI
        self.run_img = RUNNING_ZOMBI
        self.jump_img = JUMPING_ZOMBI

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurCowboy(Dinosaur):
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 450
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_COWBOY
        self.run_img = RUNNING_COWBOY
        self.jump_img = JUMPING_COWBOY

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurViking(Dinosaur):
    X_POS = 80
    Y_POS = 380
    Y_POS_DUCK = 435
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_VIKING
        self.run_img = RUNNING_VIKING
        self.jump_img = JUMPING_VIKING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurClown(Dinosaur):
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 450
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_CLOWN
        self.run_img = RUNNING_CLOWN
        self.jump_img = JUMPING_CLOWN

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_SKIN1
        self.run_img = RUNNING_SKIN1
        self.jump_img = JUMPING_SKIN1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1Winter(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_WINTER_SKIN1
        self.run_img = RUNNING_WINTER_SKIN1
        self.jump_img = JUMPING_WINTER_SKIN1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1Beach(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_BEACH_SKIN1
        self.run_img = RUNNING_BEACH_SKIN1
        self.jump_img = JUMPING_BEACH_SKIN1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1Zombi(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_SKIN1_ZOMBI
        self.run_img = RUNNING_SKIN1_ZOMBI
        self.jump_img = JUMPING_SKIN1_ZOMBI

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1Cowboy(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_COWBOY_SKIN1
        self.run_img = RUNNING_COWBOY_SKIN1
        self.jump_img = JUMPING_COWBOY_SKIN1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1Viking(Dinosaur):
    X_POS = 80
    Y_POS = 380
    Y_POS_DUCK = 435
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_VIKING_SKIN1
        self.run_img = RUNNING_VIKING_SKIN1
        self.jump_img = JUMPING_VIKING_SKIN1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin1Clown(Dinosaur):
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_CLOWN_SKIN1
        self.run_img = RUNNING_CLOWN_SKIN1
        self.jump_img = JUMPING_CLOWN_SKIN1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_SKIN3
        self.run_img = RUNNING_SKIN3
        self.jump_img = JUMPING_SKIN3

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3Winter(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_WINTER_SKIN3
        self.run_img = RUNNING_WINTER_SKIN3
        self.jump_img = JUMPING_WINTER_SKIN3

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3Beach(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_BEACH_SKIN3
        self.run_img = RUNNING_BEACH_SKIN3
        self.jump_img = JUMPING_BEACH_SKIN3

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3Zombi(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_SKIN3_ZOMBI
        self.run_img = RUNNING_SKIN3_ZOMBI
        self.jump_img = JUMPING_SKIN3_ZOMBI

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3Cowboy(Dinosaur):
    X_POS = 80
    Y_POS = 400
    Y_POS_DUCK = 445
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_COWBOY_SKIN3
        self.run_img = RUNNING_COWBOY_SKIN3
        self.jump_img = JUMPING_COWBOY_SKIN3

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3Viking(Dinosaur):
    X_POS = 80
    Y_POS = 380
    Y_POS_DUCK = 435
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_VIKING_SKIN3
        self.run_img = RUNNING_VIKING_SKIN3
        self.jump_img = JUMPING_VIKING_SKIN3

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

class DinosaurSkin3Clown(Dinosaur):
    X_POS = 80
    Y_POS = 395
    Y_POS_DUCK = 440
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_CLOWN_SKIN3
        self.run_img = RUNNING_CLOWN_SKIN3
        self.jump_img = JUMPING_CLOWN_SKIN3

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS


class DinosaurMultiplayer1(Dinosaur):
    X_POS = 80
    Y_POS = 185
    Y_POS_DUCK = 240
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
        elif self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            JUMP_SOUND.play()
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

class DinosaurMultiplayer2(Dinosaur):
    X_POS = 80
    Y_POS = 600
    Y_POS_DUCK = 645
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING_SKIN1
        self.run_img = RUNNING_SKIN1
        self.jump_img = JUMPING_SKIN1

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
        elif self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_w] and not self.dino_jump:
            JUMP_SOUND.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_s]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False