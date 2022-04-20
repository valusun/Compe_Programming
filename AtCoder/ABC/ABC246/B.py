from math import sqrt

a, b = map(int, input().split())
c = sqrt(a**2 + b**2)
print(a / c, b / c)
