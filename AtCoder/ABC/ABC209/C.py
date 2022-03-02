N = int(input())
A = sorted(list(map(int,input().split())))

Ans = A[0]
MOD = 10**9+7
for i in range(1, N):
    Ans *= (A[i]-i)
    Ans%=MOD
print(Ans)