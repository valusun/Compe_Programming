from bisect import bisect_left

N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))

Ans = 10**9
for i in range(N):
    X = bisect_left(B,A[i])
    if X==0:
        Ans = min(Ans, abs(A[i]-B[X]))
    elif X==M:
        Ans = min(Ans, abs(A[i]-B[X-1]))
    else:
        Ans = min(Ans, min(abs(A[i]-B[X]), abs(A[i]-B[X-1])))

print(Ans)