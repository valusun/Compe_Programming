def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def main():
    N = int(input())
    Coordinate = [list(map(int, input().split())) for _ in range(N)]
    ans = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            x1, y1 = Coordinate[i]
            x2, y2 = Coordinate[j]
            x = x1 - x2
            y = y1 - y2
            if x == 0:
                ans.add((0, y // abs(y)))
            elif y == 0:
                ans.add((x // abs(x), 0))
            else:
                z = abs(gcd(x, y))
                ans.add((x // z, y // z))
    print(len(ans))


if __name__ == "__main__":
    main()
