import math
def regpoarea(n, side):
    return (n * side**2) / (4 * math.tan(math.pi / n))

n = int(input())
side = float(input())

area = regpoarea(n, side)

print(area)
