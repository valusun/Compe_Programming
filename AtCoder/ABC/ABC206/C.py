from collections import Counter

N = int(input())
A = list(map(int,input().split()))

A = Counter(A)
Ans = N*(N-1)//2
for i,j in A.items():
    if j>1:
        Ans -= j*(j-1)//2
print(Ans)