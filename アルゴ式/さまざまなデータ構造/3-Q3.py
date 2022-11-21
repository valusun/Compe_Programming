import numpy as np


def main():
    H, W, x, y = map(int, input().split())
    fields = np.array([list(input()) for _ in range(H)])
    extraction = fields[x - 1 : x + 2, y - 1 : y + 2]
    for ex in extraction:
        print(*ex, sep="")


if __name__ == "__main__":
    main()
