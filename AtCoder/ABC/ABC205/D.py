from bisect import bisect_left

N,Q = map(int,input().split())
A = list(map(int,input().split()))

# A[i]までで使える整数の個数
B = []
for i in range(N):
    B.append(A[i]-(i+1))

for i in range(Q):
    k =int(input())
    x = bisect_left(B, k)
    if x==N:
        print(A[N-1]+(k-B[N-1]))
    else:
        print((A[x]-1)-(B[x]-k))