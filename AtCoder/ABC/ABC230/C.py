N,A,B = map(int, input().split())
P,Q,R,S = map(int, input().split())

Field = [["."]*(S-R+1) for _ in range(Q-P+1)]

min_k = max(P-A, R-B)
max_k = min(Q-A, S-B)

for k in range(min_k, max_k+1):
    Field[A+k-P][B+k-R] = "#"

min_k = max(P-A, B-S)
max_k = min(Q-A, B-R)

for k in range(min_k, max_k+1):
    Field[A+k-P][B-k-R] = "#"

for i in range(Q-P+1):
    print(*Field[i], sep="")