import math
def conv(degree):
    return degree * (math.pi / 180)

degree = float(input())
radian = conv(degree)

print(radian)