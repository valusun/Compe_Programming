from typing import NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int


def main():
    H, W, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    N = H * W + 1

    # 座標
    xy = [0] * (N)
    for i in range(H):
        for j in range(W):
            xy[A[i][j]] = Coordinate(i, j)

    # 累積和
    cusum = [0] * (N)
    for i in range(D + 1, N):
        j = i - D
        cusum[i] = cusum[j] + abs(xy[i].x - xy[j].x) + abs(xy[i].y - xy[j].y)

    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        print(cusum[R] - cusum[L])


if __name__ == "__main__":
    main()
