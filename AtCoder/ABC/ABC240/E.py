import sys
sys.setrecursionlimit(10**9)

N = int(input())
edge = [[] for _ in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

ans = [[10**10,-1] for _ in range(N)]
leaf_cnt = 0
def dfs(v, bef):
    global leaf_cnt
    is_leaf = True
    l = r = leaf_cnt+1
    for u in edge[v]:
        if u==bef:
            continue
        is_leaf = False
        dfs(u, v)
        l = min(l, ans[u][0])
        r = max(r, ans[u][1])
    if is_leaf:
        leaf_cnt+=1
    ans[v] = [l,r]

dfs(0, -1)
for i in range(N):
    print(*ans[i])