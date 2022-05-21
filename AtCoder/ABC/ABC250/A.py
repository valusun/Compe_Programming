def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    R, C = R - 1, C - 1
    if 0 <= R < H:
        if 0 <= C - 1 < W:
            ans += 1
        if 0 <= C + 1 < W:
            ans += 1
    if 0 <= C < W:
        if 0 <= R - 1 < H:
            ans += 1
        if 0 <= R + 1 < H:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
