

def aabb(rect1, rect2):
    return (rect1[0] + rect1[2] > rect2[0] and rect1[0] + rect1[0] < rect2[0] + rect2[2] and
            rect1[1] + rect1[3] > rect2[1] and rect1[1] + rect1[3] < rect2[1] + rect2[3])

