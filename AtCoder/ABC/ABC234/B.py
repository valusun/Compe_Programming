from math import sqrt

N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]

Ans = 0
for i in range(N):
    for j in range(i+1, N):
        res = sqrt((xy[j][0]-xy[i][0])**2 + (xy[j][1]-xy[i][1])**2)
        Ans = max(Ans, res)

print(Ans)