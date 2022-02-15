N,P = map(int,input().split())
A = list(map(int,input().split()))

Ans = 0
for i in range(N):
    if A[i] < P:
        Ans+=1

print(Ans)