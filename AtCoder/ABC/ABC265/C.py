import sys

sys.setrecursionlimit(10**9)


def main():
    def dfs(x, y):
        pattern = Grid[x][y]
        nx, ny = x + moved_pattern[pattern][0], y + moved_pattern[pattern][1]
        if 0 <= nx < H and 0 <= ny < W:
            if (nx, ny) in seen:
                print(-1)
                exit()
            seen.add((x, y))
            dfs(nx, ny)
        else:
            print(x + 1, y + 1)
            exit()

    H, W = map(int, input().split())
    Grid = [list(input()) for _ in range(H)]
    seen = set((0, 0))
    moved_pattern = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    dfs(0, 0)


if __name__ == "__main__":
    main()
