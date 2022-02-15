N,M = map(int,input().split())
A = [list(input()) for _ in range(N*2)]

def Check(x, y):
    if x==y:
        return -1
    elif x=='G' and y=='C' or x=='C' and y=='P' or x=='P' and y=='G':
        return 0
    else:
        return 1

Ans = [[0, i] for i in range(N*2)]
for i in range(M):
    for j in range(N):
        x = Ans[j*2][1]
        y = Ans[j*2+1][1]
        res = Check(A[x][i], A[y][i])
        if res != -1:
            Ans[j*2+res][0] -= 1
    Ans.sort()

for i,j in Ans:
    print(j+1)