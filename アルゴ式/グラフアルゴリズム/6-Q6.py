from collections import deque


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)

    def bfs(v):
        Q = deque()
        Q.append(v)
        dist = [-1] * N
        dist[v] = 0
        while Q:
            u = Q.popleft()
            for w in Graph[u]:
                if dist[w] != -1:
                    continue
                dist[w] = dist[u] + 1
                Q.append(w)
        return dist.index(max(dist)), max(dist)

    diam = bfs(bfs(0)[0])[1]
    print((diam + 1) // 2)


if __name__ == "__main__":
    main()
