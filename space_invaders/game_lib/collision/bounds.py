


def withinBounds(rect: tuple, width: int, height: int) -> bool:
    return rect[0] + rect[2] > width or rect[0] < 0 or rect[1] + rect[3] > height or rect[1] < 0