from collections import deque


def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    patterns = set()
    for i in range(N):
        for j in range(N):
            if i * i + j * j == M:
                patterns.add((i, j))
                patterns.add((-i, j))
                patterns.add((i, -j))
                patterns.add((-i, -j))
    Q = deque()
    Q.append((0, 0))
    ans[0][0] = 0
    while Q:
        x, y = Q.popleft()
        for px, py in patterns:
            nx = x + px
            ny = y + py
            if 0 <= nx < N and 0 <= ny < N and ans[nx][ny] == -1:
                ans[nx][ny] = ans[x][y] + 1
                Q.append((nx, ny))
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
