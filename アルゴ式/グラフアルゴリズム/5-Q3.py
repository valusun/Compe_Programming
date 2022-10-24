from collections import deque


def main():
    N, M, S, G = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[a].append(b)
    prev = [-1] * N
    visited = [False] * N
    visited[S] = True
    Q = deque()
    Q.append(S)
    while Q:
        v = Q.popleft()
        for u in Graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            prev[u] = v
            Q.append(u)
    ans = [G]
    while ans[-1] != S:
        ans.append(prev[ans[-1]])
    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
