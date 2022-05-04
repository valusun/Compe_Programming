import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    goings_towns = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        goings_towns[a - 1].append(b - 1)
    ans = 0

    def dfs(v):
        if not visited[v]:
            visited[v] = True
            for u in goings_towns[v]:
                dfs(u)

    for start in range(N):
        visited = [False] * N
        dfs(start)
        ans += sum(visited)
    print(ans)


if __name__ == "__main__":
    main()
