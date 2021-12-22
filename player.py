import pygame
from laser import Laser


class Player(pygame.sprite.Sprite):     #子类Player继承父类
    def __init__(self,pos,constraint,speed):        #这三个参数都来字主函数中的变量player_sprite
        super().__init__()  #继承
        self.image = pygame.image.load('D:\学习资料\python\space invader game\graphics\player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 100          #冷却时间
        self.lasers = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('audio/laser.wav')
        self.laser_sound.set_volume(0.5)



    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if keys[pygame.K_SPACE]:
            if self.ready:
                self.shoot_laser()
                self.laser_sound.play()
                pygame.key.set_repeat(10, 15)       #解决一键多次响应问题
            self.ready = False
            self.laser_time = pygame.time.get_ticks()


    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True


    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()