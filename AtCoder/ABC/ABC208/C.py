N,K = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(A)

Base = K//N
K%=N
if K==0:
    Bias=0
else:
    Bias=B[K-1]

for i in range(N):
    if A[i]<=Bias:
        print(Base+1)
    else:
        print(Base)