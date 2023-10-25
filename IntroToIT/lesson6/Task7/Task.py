#INTRO TO IT 2nd COURSE
import math
def heron_triangle_area(a, b, c):
    import math
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))