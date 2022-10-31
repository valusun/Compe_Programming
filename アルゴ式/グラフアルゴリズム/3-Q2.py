from collections import deque


def main():
    N, M = map(int, input().split())
    Friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Friends[a].append(b)
        Friends[b].append(a)
    dist = [-1] * N
    dist[0] = 0
    Q = deque()
    Q.append(0)
    while Q:
        v = Q.popleft()
        for nv in Friends[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            Q.append(nv)
    print(max(dist))


if __name__ == "__main__":
    main()
