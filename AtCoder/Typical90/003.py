from collections import deque


def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    def GetFurthestFromV(v):
        """入力地点から最も遠い地点と距離を返す"""
        que = deque()
        que.append(v)
        dist = [-1] * N
        dist[v] = 0
        point = 0
        while que:
            u = que.popleft()
            for w in graph[u]:
                if dist[w] != -1:
                    continue
                dist[w] = dist[u] + 1
                point = w
                que.append(w)
        return point, max(dist)

    _, ans = GetFurthestFromV(GetFurthestFromV(0)[0])
    print(ans + 1)


if __name__ == "__main__":
    main()
