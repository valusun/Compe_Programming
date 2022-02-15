from itertools import permutations

N,M = map(int,input().split())
AB = [[False]*N for _ in range(N)]
CD = [[False]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    AB[a-1][b-1] = True
    AB[b-1][a-1] = True
for _ in range(M):
    c,d = map(int,input().split())
    CD[c-1][d-1] = True
    CD[d-1][c-1] = True

for p in permutations(range(N)):
    Flag = True
    for i in range(N):
        for j in range(N):
            if AB[i][j] != CD[p[i]][p[j]]:
                Flag = False
                break
        if Flag == False:
            break
    if Flag:
        print("Yes")
        break
else:
    print("No")