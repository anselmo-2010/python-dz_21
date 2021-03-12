import math

def square(arg):
    s = arg ** 2
    p = arg * 4
    d = arg * math.sqrt(2)
    d = round(d, 1)
    return s, p, d

print(square(5))
