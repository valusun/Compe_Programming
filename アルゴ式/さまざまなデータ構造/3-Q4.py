import numpy as np


def main():
    H, W = map(int, input().split())
    fields = np.array([list(input()) for _ in range(H)])
    r, c = map(int, input().split())
    ans = np.count_nonzero(fields[r, :] == "#")
    ans += np.count_nonzero(fields[:, c] == "#")
    print(ans - (fields[r][c] == "#"))


if __name__ == "__main__":
    main()
