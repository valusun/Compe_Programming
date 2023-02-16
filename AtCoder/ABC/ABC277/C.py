from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    from_to = defaultdict(list)
    for _ in range(N):
        a, b = map(int, input().split())
        from_to[a].append(b)
        from_to[b].append(a)
    ans = 1
    visited = set()

    def dfs(k):
        nonlocal ans
        visited.add(k)
        ans = max(ans, k)
        for nk in from_to[k]:
            if nk in visited:
                continue
            dfs(nk)

    dfs(1)
    print(ans)


if __name__ == "__main__":
    main()
