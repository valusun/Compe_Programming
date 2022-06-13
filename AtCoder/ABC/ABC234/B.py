from math import sqrt


def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = xy[i][0], xy[i][1]
            x2, y2 = xy[j][0], xy[j][1]
            ans = max(ans, sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
    print(ans)


if __name__ == "__main__":
    main()
