def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)

    operated = [[] for _ in range(N)]
    operated[0].append(0)
    visited = [False] * N
    visited[0] = True
    for i in range(N):
        for j in operated[i]:
            for v in Graph[j]:
                if visited[v]:
                    continue
                visited[v] = True
                operated[i + 1].append(v)
    for ans in operated:
        print(*sorted(ans))


if __name__ == "__main__":
    main()
