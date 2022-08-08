from collections import namedtuple


def main():
    N, K = map(int, input().split())
    Coordinate = namedtuple("Coordinate", "x y")
    xy = []
    x, y = [], []
    for _ in range(N):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        xy.append(Coordinate(x_, y_))
    x.sort()
    y.sort()
    min_area = 10**20
    for sx in range(N):
        for gx in range(sx + 1, N):
            for sy in range(N):
                for gy in range(sy + 1, N):
                    contains = 0
                    for i in range(N):
                        if x[sx] <= xy[i].x <= x[gx] and y[sy] <= xy[i].y <= y[gy]:
                            contains += 1

                    if contains == K:
                        min_area = min(min_area, (x[gx] - x[sx]) * (y[gy] - y[sy]))
    print(min_area)


if __name__ == "__main__":
    main()
