def CheckDuplication(n):
    if n[0] == n[1]:
        return n[2]
    elif n[1] == n[2]:
        return n[0]
    else:
        return n[1]


x, y = [], []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print(CheckDuplication(x), CheckDuplication(y))
