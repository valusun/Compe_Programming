import itertools
from math import sqrt


def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    res = cnt = 0
    for p in itertools.permutations(xy):
        cnt += 1
        for i in range(1, N):
            res += sqrt((p[i - 1][0] - p[i][0]) ** 2 + (p[i - 1][1] - p[i][1]) ** 2)
    print(res / cnt)


if __name__ == "__main__":
    main()
