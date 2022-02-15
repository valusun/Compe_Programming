from bisect import bisect_left

N,Q = map(int,input().split())
A = sorted(list(map(int,input().split())))

for _ in range(Q):
    print(N - bisect_left(A, int(input())))