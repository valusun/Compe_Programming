from collections import deque


def main():
    def IsMovable(h, w):
        return 0 <= h < H and 0 <= w < W and fields[h][w] == "."

    H, W = map(int, input().split())
    Sh, Sw = map(int, input().split())
    Gh, Gw = map(int, input().split())
    Sh, Sw, Gh, Gw = Sh - 1, Sw - 1, Gh - 1, Gw - 1
    fields = [list(input()) for _ in range(H)]
    fields_cnt = [[10**10] * W for _ in range(H)]
    fields_cnt[Sh][Sw] = 0

    no_warp = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    warp = [(h, w) for h in range(-2, 3) for w in range(-2, 3) if h != 0 or w != 0]

    que = deque()
    que.append((Sh, Sw))
    while que:
        h, w = que.popleft()
        if h == Gh and w == Gw:
            print(fields_cnt[Gh][Gw])
            break
        for mh, mw in no_warp:
            nh, nw = h + mh, w + mw
            if IsMovable(nh, nw) and fields_cnt[nh][nw] > fields_cnt[h][w]:
                fields_cnt[nh][nw] = fields_cnt[h][w]
                que.appendleft((nh, nw))
        for mh, mw in warp:
            nh, nw = h + mh, w + mw
            if IsMovable(nh, nw) and fields_cnt[nh][nw] > fields_cnt[h][w] + 1:
                fields_cnt[nh][nw] = fields_cnt[h][w] + 1
                que.append((nh, nw))
    else:
        print(-1)


if __name__ == "__main__":
    main()
