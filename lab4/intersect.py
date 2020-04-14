import math


def intersect(r1, x1, y1, r2, x2, y2):
    xDif = x1 - x2
    yDif = y1 - y2
    dist = math.sqrt(xDif * xDif + yDif * yDif)
    reach = r1 + r2
    if (reach > dist):
        print(True)
    else:
        print(False)

#intersect(5, 2, 2, 4, 3, 3)
#intersect(5,-2,5,2,0,8)
intersect(2,-2,-5,2,-2,8) 
