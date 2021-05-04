from game_lib.game import Game
from defender import Defender
from bullets import Bullets
from wall import Wall
from invaders import Invaders

class SpaceInvaders(Game):
    def __init__(self):
        super().__init__()
        self.width = 800 
        self.height = 600

    def setup(self):
        self.makeWindow(self.width, self.height)
        self.defender = Defender(150, self.height - 50)
        self.bullets = Bullets()

        self.walls = [
            Wall(( 50, 400), 15, 7),
            Wall((300, 400), 15, 7),
            Wall((550, 400), 15, 7),
        ]

        self.invaders = Invaders()


    def update(self, dt):
        self.defender.move(dt)
        self.defender.draw(self._window)
        self.defender.shoot(self.bullets, dt)

        self.bullets.move(dt, (self.width, self.height))
        self.bullets.draw(self._window)

        self.invaders.move(dt, (self.width, self.height))
        self.invaders.draw(self._window)

        for wall in self.walls:
            wall.draw(self._window)
            wall.bulletCollision(self.bullets)

if __name__ == '__main__':
    spaceInvaders = SpaceInvaders()
    spaceInvaders.init()
    spaceInvaders.start()

