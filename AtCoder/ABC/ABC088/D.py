from collections import deque


def main():
    H, W = map(int, input().split())
    Field = [list(input()) for _ in range(H)]
    black_cnt = sum([f.count("#") for f in Field])

    INF = 10**9
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]
    Q = deque()
    Q.append((0, 0))
    dist = [[INF] * W for _ in range(H)]
    dist[0][0] = 1
    while Q:
        h, w = Q.popleft()
        if h == H - 1 and w == W - 1:
            print(H * W - black_cnt - dist[-1][-1])
            exit()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W and Field[nh][nw] == ".":
                if dist[nh][nw] == INF:
                    dist[nh][nw] = dist[h][w] + 1
                    Q.append((nh, nw))
    print(-1)


if __name__ == "__main__":
    main()
