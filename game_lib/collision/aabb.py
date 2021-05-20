

def aabb(rect1: tuple, rect2: tuple) -> bool:
    ''' 
        Takes in to rectangles represented by tubles in the format of (x, y, width, height). 
        Checks if there is any overlaps at all 
    '''

    return (rect1[0] + rect1[2] > rect2[0] and rect1[0] < rect2[0] + rect2[2] and
            rect1[1] + rect1[3] > rect2[1] and rect1[1] < rect2[1] + rect2[3])

