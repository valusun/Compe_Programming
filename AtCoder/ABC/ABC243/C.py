N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
S = input()

L,R = dict(),dict()
R_set = set()
for i in range(N):
    if S[i]=='L':
        if xy[i][1] not in L:
            L[xy[i][1]] = -1
        L[xy[i][1]] = max(L[xy[i][1]], xy[i][0])
    else:
        if xy[i][1] not in R:
            R[xy[i][1]] = 10**10
        R[xy[i][1]] = min(R[xy[i][1]], xy[i][0])
        R_set.add(xy[i][1])

for x,y in L.items():
    if x in R_set:
        if y >= R[x]:
            print("Yes")
            break
else:
    print("No")