from math import sqrt


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        x, y = XY[i]
        res = float("inf")
        for a in A:
            ax, ay = XY[a - 1]
            res = min(res, sqrt((x - ax) ** 2 + (y - ay) ** 2))
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
