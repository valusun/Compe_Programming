N,X = map(int,input().split())
jump = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*(X+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(X):
        if dp[i][j]:
            if j+jump[i][0] <= X:
                dp[i+1][j+jump[i][0]] = 1
            if j+jump[i][1] <= X:
                dp[i+1][j+jump[i][1]] = 1

if dp[N][X]:
    print("Yes")
else:
    print("No")