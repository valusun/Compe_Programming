H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

for j in range(W):
    tmp = []
    for i in range(H):
        tmp.append(A[i][j])
    print(*tmp)