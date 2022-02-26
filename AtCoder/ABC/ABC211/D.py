from collections import deque

N,M = map(int,input().split())
Graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    Graph[a-1].append(b-1)
    Graph[b-1].append(a-1)

dist = [float('inf')]*N
dist[0] = 0

dist_cnt = [0]*N
dist_cnt[0] = 1

MOD = 10**9+7

Q = deque()
Q.append((0))
while Q:
    v = Q.popleft()
    for i in Graph[v]:
        if dist[i] == float('inf'):
            dist[i] = dist[v]+1
            Q.append((i))
            dist_cnt[i] = dist_cnt[v]
        elif dist[i] == dist[v]+1:
            dist_cnt[i] = (dist_cnt[i]+dist_cnt[v])%MOD

print(dist_cnt[N-1])