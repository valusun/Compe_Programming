N,M = map(int,input().split())
Data = []
for i in range(M):
    a,b,c = map(int,input().split())
    Data.append([a-1,b-1,c])

# ワーシャルフロイド法
INF = 10**10
dist = [[INF]*N for _ in range(N)]
for a,b,c in Data:
    dist[a][b] = c
    dist[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ans = 0
for a,b,c in Data:
    for i in range(N):
        if dist[i][a] + dist[i][b] <= c:
            ans+=1
            break
print(ans)