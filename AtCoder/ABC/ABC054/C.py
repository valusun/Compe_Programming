def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a - 1].append(b - 1)
        Graph[b - 1].append(a - 1)

    def dfs(v, visited):
        if False not in visited:
            return 1
        ans = 0
        for u in Graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            ans += dfs(u, visited)
            visited[u] = False
        return ans

    visited = [False] * N
    visited[0] = True
    print(dfs(0, visited))


if __name__ == "__main__":
    main()
