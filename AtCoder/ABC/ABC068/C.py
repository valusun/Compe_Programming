from collections import deque


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    visited = [False] * N
    visited[0] = True
    que = deque()
    que.append([0, 0])
    while que:
        v, d = que.popleft()
        if v == N - 1:
            print("POSSIBLE")
            break
        for u in graph[v]:
            if visited[u] or d == 2:
                continue
            visited[u] = True
            que.append([u, d + 1])
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
