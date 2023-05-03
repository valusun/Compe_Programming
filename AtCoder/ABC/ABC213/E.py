from collections import deque


def main():
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    INF = 10**9
    broken_cnt = [[INF] * W for _ in range(H)]
    normal_move_h = [0, 1, 0, -1]
    normal_move_w = [1, 0, -1, 0]
    broken_move_h = [-2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
    broken_move_w = [-1, 0, 1, -2, -1, 0, 1, 2, -2, -1, 1, 2, -2, -1, 0, 1, 2, -1, 0, 1]

    Q = deque()
    Q.append((0, 0, 0))
    while Q:
        h, w, d = Q.popleft()
        if h == (H - 1) and w == (W - 1):
            break
        if field[h][w] == ".":
            for mh, mw in zip(normal_move_h, normal_move_w):
                nh = h + mh
                nw = w + mw
                is_area = 0 <= nh < H and 0 <= nw < W
                if is_area and d < broken_cnt[nh][nw]:
                    broken_cnt[nh][nw] = d
                    Q.appendleft((nh, nw, d))
        else:
            for mh, mw in zip(broken_move_h, broken_move_w):
                nh = h + mh
                nw = w + mw
                tmp_d = d + 1
                is_area = 0 <= nh < H and 0 <= nw < W
                if is_area and tmp_d < broken_cnt[nh][nw]:
                    broken_cnt[nh][nw] = tmp_d
                    Q.append((nh, nw, tmp_d))
    print(broken_cnt[H - 1][W - 1])


if __name__ == "__main__":
    main()
