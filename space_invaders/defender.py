import pygame

class Defender(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self._width = 45
        self._height = 25
        self._speed = 300
        self._shootCounter = 0

    def getRect(self):
        return (self.x, self.y, self.width, self.height)


    def draw(self, wn):
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self._width, self._height))

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self._speed * dt
        elif keys[pygame.K_RIGHT] and self.x + self._width < 800:
            self.x += self._speed * dt

    def shoot(self, bullets: object, dt:float) -> None:
        keys = pygame.key.get_pressed()

        self._shootCounter += dt
        if keys[pygame.K_SPACE] and self._shootCounter > 0.4:
            bullets.addBullet(self.x + self._width//2, self.y, (0, -1))
            self._shootCounter = 0


            


