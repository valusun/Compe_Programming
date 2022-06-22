def main():
    W, H, N = map(int, input().split())
    sx, sy, gx, gy = 0, 0, W, H
    for _ in range(N):
        x, y, a = map(int, input().split())
        if a == 1:
            sx = max(sx, x)
        elif a == 2:
            gx = min(gx, x)
        elif a == 3:
            sy = max(sy, y)
        else:
            gy = min(gy, y)
    print(max(0, (gx - sx) * max(0, (gy - sy))))


if __name__ == "__main__":
    main()
