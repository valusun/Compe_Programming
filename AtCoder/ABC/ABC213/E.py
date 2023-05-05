from collections import deque


def main():
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    field_cnt = [[10**9] * W for _ in range(H)]
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]
    warp_dh = [-2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
    warp_dw = [1, 0, -1, 2, 1, 0, -1, -2, 2, 1, -1, -2, 2, 1, 0, -1, -2, 1, 0, -1]
    Q = deque()
    Q.append((0, 0, 0))
    while Q:
        h, w, d = Q.popleft()
        if h == H - 1 and w == W - 1:
            break
        for mh, mw in zip(dh, dw):
            nh = h + mh
            nw = w + mw
            is_area = 0 <= nh < H and 0 <= nw < W
            if is_area and field[nh][nw] == "." and d < field_cnt[nh][nw]:
                field_cnt[nh][nw] = d
                Q.appendleft((nh, nw, d))  # 優先的に見るため、すぐ取り出せる先頭に入れる
        # 体力1を消費して、2x2の範囲に移動できると見なす
        for mh, mw in zip(warp_dh, warp_dw):
            nh = h + mh
            nw = w + mw
            is_area = 0 <= nh < H and 0 <= nw < W
            if is_area and d + 1 < field_cnt[nh][nw]:
                field_cnt[nh][nw] = d + 1
                Q.append((nh, nw, d + 1))
    print(field_cnt[H - 1][W - 1])


if __name__ == "__main__":
    main()
