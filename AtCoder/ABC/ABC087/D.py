from collections import deque


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        l, r, d = map(int, input().split())
        Graph[l - 1].append([r - 1, d])
        Graph[r - 1].append([l - 1, -d])
    INF = 10**9
    dist = [INF] * N
    for i in range(N):
        if dist[i] != INF:
            continue
        Q = deque()
        Q.append(i)
        dist[i] = 0
        while Q:
            v = Q.popleft()
            for nv, nd in Graph[v]:
                if dist[nv] == INF:
                    dist[nv] = dist[v] + nd
                    Q.append(nv)
                else:
                    if dist[nv] != dist[v] + nd:
                        print("No")
                        exit()
    print("Yes")


if __name__ == "__main__":
    main()
