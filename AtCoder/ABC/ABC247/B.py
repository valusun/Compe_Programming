from collections import Counter

N = int(input())
c = []
for i in range(N):
    s, t = input().split()
    c.append(s)
    c.append(t)
c = Counter(c)
if c.most_common()[1][1] >= 2:
    print("No")
else:
    print("Yes")
