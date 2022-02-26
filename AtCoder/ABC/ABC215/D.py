from math import sqrt

N,M = map(int,input().split())
A = list(map(int,input().split()))

# 素因数
S = set()
for i in range(N):
    for j in range(2, int(sqrt(A[i]))+1):
        while A[i]%j==0:
            S.add(j)
            A[i]//=j
    if A[i]!=1:
        S.add(A[i])

# 削る
Number = [0]*(M+1)
for i in S:
    j = i
    while j<=M:
        Number[j] = 1
        j+=i

Ans = []
for i in range(1, M+1):
    if Number[i] == 0:
        Ans.append(i)

print(len(Ans), *Ans, sep="\n")