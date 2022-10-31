from collections import deque


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)

    def bfs(s):
        Q = deque()
        Q.append(s)
        dist = [-1] * N
        dist[s] = 0
        while Q:
            v = Q.popleft()
            for nv in Graph[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + 1
                Q.append(nv)
        return dist.index(max(dist)), max(dist)

    diam = bfs(bfs(0)[0])[1]
    print((diam + 1) // 2)


if __name__ == "__main__":
    main()
