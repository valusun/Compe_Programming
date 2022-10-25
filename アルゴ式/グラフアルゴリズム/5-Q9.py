from collections import deque


def main():
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    cnt = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        Graph[b].append(a)
        cnt[a] += 1
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
            if cnt[u] == 0:
                Q.append(u)

    print("No" if len(ans) == N else "Yes")


if __name__ == "__main__":
    main()
