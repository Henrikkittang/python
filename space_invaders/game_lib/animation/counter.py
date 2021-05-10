

class Counter(object):
    def __init__(self):
        self._counter = 0 

    def reset(self):
        self._counter = 0

    def __repr__(self):
        return str(self._counter)

    def __call__(self, dt: float, value: float) -> bool:
        self._counter += dt
        if self._counter >= value:
            self._counter = 0
            return True
        return False