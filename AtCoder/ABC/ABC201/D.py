H,W = map(int,input().split())
A = [list(input()) for _ in range(H)]

def GetPoint(i,j):
    if A[i][j]=='+':
        return 1
    else:
        return -1

dp = [[-10**10]*W for _ in range(H)]
dp[H-1][W-1] = 0

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        # 下
        if i<H-1:
            Point = GetPoint(i+1,j)
            dp[i][j] = max(dp[i][j], Point-dp[i+1][j])
        # 右
        if j<W-1:
            Point = GetPoint(i,j+1)
            dp[i][j] = max(dp[i][j], Point-dp[i][j+1])

if dp[0][0]>0:
    print("Takahashi")
elif dp[0][0]<0:
    print("Aoki")
else:
    print("Draw")