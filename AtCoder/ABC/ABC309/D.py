from collections import deque


def main():
    N1, N2, M = map(int, input().split())
    graph = [[] for _ in range(N1 + N2)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    visited = [-1] * (N1 + N2)

    def bfs(u, c):
        Q = deque()
        Q.append((u, c))
        visited[u] = c
        while Q:
            u, c = Q.popleft()
            for v in graph[u]:
                if visited[v] != -1:
                    continue
                visited[v] = c + 1
                Q.append((v, c + 1))

    bfs(0, 0)
    bfs(N1 + N2 - 1, 0)
    print(max(visited[:N1]) + max(visited[N1:]) + 1)


if __name__ == "__main__":
    main()
