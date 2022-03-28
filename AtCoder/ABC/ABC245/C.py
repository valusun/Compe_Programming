N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a_dp = [0]*N
b_dp = [0]*N

a_dp[0] = 1
b_dp[0] = 1

for i in range(1, N):
    if a_dp[i-1]:
        if abs(A[i-1]-A[i])<=K: a_dp[i]=1
        if abs(A[i-1]-B[i])<=K: b_dp[i]=1
    if b_dp[i-1]:
        if abs(B[i-1]-A[i])<=K: a_dp[i]=1
        if abs(B[i-1]-B[i])<=K: b_dp[i]=1

if a_dp[N-1] or b_dp[N-1]:
    print("Yes")
else:
    print("No")