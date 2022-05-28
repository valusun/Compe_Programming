from heapq import heappush, heappop


def main():
    N, M = map(int, input().split())
    before_cnts = [0] * N
    after_elements = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        before_cnts[b - 1] += 1
        after_elements[a - 1].append(b - 1)
    que = []
    for i, v in enumerate(before_cnts):
        if not v:
            heappush(que, i)
    ans = []
    while que:
        v = heappop(que)
        ans.append(v + 1)
        for u in after_elements[v]:
            before_cnts[u] -= 1
            if not before_cnts[u]:
                heappush(que, u)
    if len(ans) == N:
        print(*ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
