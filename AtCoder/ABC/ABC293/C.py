def main():
    H, W = map(int, input().split())
    fields = [list(map(str, input().split())) for _ in range(H)]
    ans = 0

    def dfs(h, w, memo):
        nonlocal ans
        if h == H - 1 and w == W - 1:
            ans += 1
            return
        for dh, dw in ((0, 1), (1, 0)):
            nh, nw = h + dh, w + dw
            is_area = 0 <= nh < H and 0 <= nw < W
            if is_area and fields[nh][nw] not in memo:
                mm = memo | set([fields[nh][nw]])
                dfs(nh, nw, mm)

    dfs(0, 0, set([fields[0][0]]))
    print(ans)


if __name__ == "__main__":
    main()
