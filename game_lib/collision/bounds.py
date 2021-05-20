


def withinBounds(rect: tuple, width: int, height: int) -> bool:
    '''
        Checks if rect is fully inside the bounds of a larger rectangle with 
        x and y as (0, 0) aka. the top left corner of the screen. Most usefull for 
        bound-checking within the global screen context 
    '''
    return rect[0] + rect[2] > width or rect[0] < 0 or rect[1] + rect[3] > height or rect[1] < 0