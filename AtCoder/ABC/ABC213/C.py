from bisect import bisect_left

H,W,N = map(int,input().split())
A = []
H_idx,W_idx = set(),set()
for i in range(N):
    h,w = map(int,input().split())
    H_idx.add(h)
    W_idx.add(w)
    A.append([h,w])

H_idx = sorted(list(H_idx))
W_idx = sorted(list(W_idx))
for i in range(N):
    print(bisect_left(H_idx,A[i][0])+1, bisect_left(W_idx,A[i][1])+1)