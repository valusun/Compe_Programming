import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
Graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    Graph[a-1].append(b-1)

def dfs(v):
    visited[v] = True
    for i in Graph[v]:
        if visited[i] == False:
            dfs(i)

ans = 0
for i in range(N):
    visited = [False]*N
    dfs(i)
    ans += sum(visited)

print(ans)
