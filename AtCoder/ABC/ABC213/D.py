import sys
sys.setrecursionlimit(10**9)

N = int(input())
Graph = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    Graph[a-1].append(b-1)
    Graph[b-1].append(a-1)
for i in range(N):
    Graph[i].sort()

visited = [False]*N
Ans = []
def dfs(v):
    Ans.append(v+1)
    visited[v]=True
    for i in Graph[v]:
        if visited[i]:
            continue
        dfs(i)
        Ans.append(v+1)

dfs(0)
print(*Ans)