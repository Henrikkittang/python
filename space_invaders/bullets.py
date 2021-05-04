import pygame

class Bullet(object):
    def __init__(self, x, y, direction):
        self.x = x 
        self.y = y
        self._direction = direction
        self._speed = 500
    
    def getRect(self) -> tuple:
        return (self.x, self.y, self.width, self.height)

    def draw(self, wn: object) -> None:
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, 5, 15))

    def move(self, dt: float) -> None:
        self.x += self._speed * self._direction[0] * dt 
        self.y += self._speed * self._direction[1] * dt 


class Bullets():
    def __init__(self):
        self._bullets = []

    def __iter__(self):
        for bullet in self._bullets:
            yield (bullet.x, bullet.y)

    def draw(self, wn: object) -> None:
        [bullet.draw(wn) for bullet in self._bullets]
       
    def move(self, dt: float, screenDimensions: tuple) -> None:
        for idx, bullet in enumerate(self._bullets):
            bullet.move(dt)
            if bullet.y < 0 or bullet.y > screenDimensions[1]:
                self._bullets.pop(idx)

    def addBullet(self, x, y, direction: tuple) -> None:
        self._bullets.append( Bullet(x, y, direction) )

    def popBullet(self, idx):
        self._bullets.pop(idx)






