def CutWidth(h: int, w: int):
    b = (h // 2) * w
    c = (h - (h // 2)) * w
    return b, c


def CutHeight(h: int, w: int):
    b = h * (w // 2)
    c = h * (w - (w // 2))
    return b, c


def main():
    H, W = map(int, input().split())
    ans = float("inf")

    # Aを横一列に切る
    for i in range(1, H):
        a = i * W
        b, c = CutHeight(H - i, W)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        b, c = CutWidth(H - i, W)
        ans = min(ans, max(a, b, c) - min(a, b, c))

    for i in range(1, W):
        a = H * i
        b, c = CutHeight(H, W - i)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        b, c = CutWidth(H, W - i)
        ans = min(ans, max(a, b, c) - min(a, b, c))

    print(ans)


if __name__ == "__main__":
    main()
