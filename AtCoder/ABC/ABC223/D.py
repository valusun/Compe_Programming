import heapq

N,M = map(int,input().split())
AB = [[] for _ in range(N)]
cnt = [0]*N
for i in range(M):
    a,b = map(int,input().split())
    AB[a-1].append(b-1)
    cnt[b-1]+=1

A = []
for i in range(N):
    if cnt[i] == 0:
        A.append(i)

heapq.heapify(A)

Ans = []
while A:
    x = heapq.heappop(A)
    Ans.append(x+1)
    for v in AB[x]:
        cnt[v]-=1
        if cnt[v] == 0: 
            heapq.heappush(A, v)

if len(Ans) == N:
    print(*Ans)
else:
    print(-1)