N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

MAX = 3001
MOD = 998244353

dp = [[0]*(MAX) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N+1):
    for j in range(MAX-1):
        dp[i][j+1] += dp[i][j]
        dp[i][j+1]%=MOD
    if i!=N:
        for j in range(A[i], B[i]+1):
            dp[i+1][j] += dp[i][j]

print(dp[N][MAX-1])