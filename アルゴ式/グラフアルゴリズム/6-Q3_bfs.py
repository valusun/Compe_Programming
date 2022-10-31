from collections import deque


def main():
    N = int(input())
    Graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    depth = [-1] * N

    Q = deque()
    Q.append(0)
    depth[0] = 0
    while Q:
        v = Q.popleft()
        for nv in Graph[v]:
            if depth[nv] != -1:
                continue
            depth[nv] = depth[v] + 1
            Q.append(nv)
    print(max(depth))


if __name__ == "__main__":
    main()
