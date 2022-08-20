import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    ans = [[0] * N for _ in range(2)]
    ans[0][0] = A[0][0]

    def dfs(x, y):
        if x == 1 and y == N - 1:
            return
        for i, j in [(0, 1), (1, 0)]:
            nx = x + i
            ny = y + j
            if 0 <= nx < 2 and 0 <= ny < N:
                ans[nx][ny] = max(ans[nx][ny], A[nx][ny] + ans[x][y])
                dfs(nx, ny)

    dfs(0, 0)
    print(ans[-1][-1])


if __name__ == "__main__":
    main()
