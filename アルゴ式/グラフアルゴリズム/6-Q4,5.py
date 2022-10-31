from collections import deque
from typing import Tuple


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)

    def bfs(s) -> Tuple[int, int]:
        Q: deque = deque()
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

    idx, _ = bfs(0)
    print(bfs(idx)[1])


if __name__ == "__main__":
    main()
