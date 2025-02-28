import math
def traparea(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input())
base1 = float(input())
base2 = float(input())

area = traparea(height, base1, base2)

print(area)