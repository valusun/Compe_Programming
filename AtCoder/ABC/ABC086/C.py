def main():
    N = int(input())
    pt, px, py = 0, 0, 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        dist = abs(px - x) + abs(py - y)
        if t - pt < dist or (t - pt - dist) % 2:
            print("No")
            exit()
        pt, px, py = t, x, y
    print("Yes")


if __name__ == "__main__":
    main()
