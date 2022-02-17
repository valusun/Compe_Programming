N = int(input())
A = list(map(int,input().split()))

dp = [[0]*10 for _ in range(N)]
dp[0][A[0]] = 1

MOD = 998244353

for i in range(N-1):
    for j in range(10):
        if dp[i][j]:
            F = (j+A[i+1])%10
            G = (j*A[i+1])%10
            dp[i+1][F] = (dp[i+1][F]+dp[i][j])%MOD
            dp[i+1][G] = (dp[i+1][G]+dp[i][j])%MOD

for i in range(10):
    print(dp[N-1][i])