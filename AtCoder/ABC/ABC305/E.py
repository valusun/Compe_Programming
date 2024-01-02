import heapq

INF = -(10**18)


def main():
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    mx_hp = [INF] * N
    guards = []
    for _ in range(K):
        p, h = map(int, input().split())
        mx_hp[p - 1] = h
        heapq.heappush(guards, (-h, p - 1))
    while guards:
        h, p = heapq.heappop(guards)
        h = -h
        if mx_hp[p] != h:
            continue
        for nxt_p in graph[p]:
            if mx_hp[nxt_p] >= h - 1:
                continue
            mx_hp[nxt_p] = h - 1
            heapq.heappush(guards, (-(h - 1), nxt_p))
    ans = [i + 1 for i, n in enumerate(mx_hp) if n >= 0]
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
