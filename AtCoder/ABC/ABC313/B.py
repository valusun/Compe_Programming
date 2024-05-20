from collections import defaultdict


def main():
    N, M = map(int, input().split())
    AB = list(map(int, input().split()) for _ in range(M))
    memo1 = defaultdict(list)
    for a, b in AB:
        memo1[a - 1].append(b - 1)

    memo2 = [set() for _ in range(N)]

    def dfs(n):
        if memo2[n]:
            return memo2[n]
        for x in memo1[n]:
            memo2[n].add(x)
            k = dfs(x)
            memo2[n] |= k
        return memo2[n]

    for i in range(N):
        for x in memo1[i]:
            memo2[i].add(x)
            memo2[i] |= dfs(x)
    length = [len(x) for x in memo2]
    mx = max(length)
    if mx == N - 1 and length.count(mx) == 1:
        print(length.index(mx) + 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
