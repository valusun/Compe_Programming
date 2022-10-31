from collections import deque


def main():
    N, M, S, G = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
    visited = [False] * N
    visited[S] = True
    Q = deque()
    Q.append(S)
    while Q:
        v = Q.popleft()
        if v == G:
            print("Yes")
            exit()
        for nv in Graph[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            Q.append(nv)
    print("No")


if __name__ == "__main__":
    main()
