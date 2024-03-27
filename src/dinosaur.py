from assets import *

class Dinosaur:
    X_POS = 80
    Y_POS = 390
    Y_POS_DUCK = 460
    JUMP_VEL = 9

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
    JUMP_VEL = 9

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
    JUMP_VEL = 9

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
    Y_POS_DUCK = 460
    JUMP_VEL = 9

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
