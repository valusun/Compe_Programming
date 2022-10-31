def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
    for i in range(N):
        Graph[i] = sorted(Graph[i])
    ans = []
    visited = [False] * N

    def dfs(v):
        visited[v] = True
        for nv in Graph[v]:
            if visited[nv]:
                continue
            dfs(nv)
        ans.append(v)

    for v in range(N):
        if visited[v]:
            continue
        dfs(v)
    print(*ans[::-1])


if __name__ == "__main__":
    main()
