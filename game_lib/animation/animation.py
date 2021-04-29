


class Animation(object):
    def __init__(self, steps: int, speed: float):
        self._steps     : int   = steps
        self._speed     : float = speed
        self._animations: list  = []
        self._counter   : float = 0
    
    def reset(self) -> None:
        self._counter = 0

    def update(self, dt: float):
        self._counter += dt

        idx = int(self._animationCounter // self._speed)
        if idx >= self._steps: 
            idx = self._animationCounter = 0

        return self._animations[idx]


    


