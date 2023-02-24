import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    BIAS = 1000
    field = [[0] * 2001 for _ in range(2001)]
    for _ in range(N):
        x, y = map(int, input().split())
        field[x + BIAS][y + BIAS] = 1
    visited = [[0] * 2001 for _ in range(2001)]

    dx = [0, 0, 1, 1, -1, -1]
    dy = [-1, 1, 0, 1, -1, 0]

    def dfs(x, y):
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            is_area = 0 <= nx <= 2000 and 0 <= ny <= 2000
            if is_area and visited[nx][ny] == 0 and field[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny)

    ans = 0
    for i in range(2001):
        for j in range(2001):
            if visited[i][j] == 0 and field[i][j]:
                visited[i][j] = 1
                ans += 1
                dfs(i, j)
    print(ans)


if __name__ == "__main__":
    main()
