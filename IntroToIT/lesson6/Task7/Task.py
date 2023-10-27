#INTRO TO IT 2nd COURSE
def heron_triangle_area(a, b, c):
    s = math.sqrt(a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c)) ** 0.5