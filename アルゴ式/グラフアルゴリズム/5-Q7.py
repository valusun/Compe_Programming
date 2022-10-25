from collections import deque


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    cnt = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[b].append(a)
        cnt[a] += 1
    for i in range(N):
        Graph[i] = sorted(Graph[i])

    Q = deque()
    for i, c in enumerate(cnt):
        if c == 0:
            Q.append(i)

    ans = []
    while Q:
        v = Q.popleft()
        ans.append(v)
        for u in Graph[v]:
            cnt[u] -= 1
            if not cnt[u]:
                Q.append(u)
    print(*ans[::-1])


if __name__ == "__main__":
    main()
