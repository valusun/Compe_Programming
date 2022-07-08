def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY.sort()
    start, end = XY[0]
    for x, y in XY[1:]:
        if x > end:
            print(start, end)
            start = x
            end = y
        end = max(end, y)
    print(start, end)


if __name__ == "__main__":
    main()
