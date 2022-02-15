N,Q = map(int,input().split())
A = list(map(int,input().split()))

dic = dict()
for i in range(N):
    if A[i] not in dic:
        dic[A[i]] = []
    dic[A[i]].append(i+1)

for i in range(Q):
    x,k = map(int,input().split())
    if x not in dic or len(dic[x]) < k:
        print(-1)
    else:
        print(dic[x][k-1])