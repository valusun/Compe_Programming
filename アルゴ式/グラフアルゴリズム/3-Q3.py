from collections import deque


def main():
    H, W = map(int, input().split())
    sh, sw, gh, gw = map(int, input().split())
    Fields = [list(input()) for _ in range(H)]
    dist = [[-1] * W for _ in range(H)]

    dh = [-1, 0, 1, 0]
    dw = [0, -1, 0, 1]

    Q = deque()
    Q.append((sh, sw))
    dist[sh][sw] = 0
    while Q:
        h, w = Q.popleft()
        if h == gh and w == gw:
            break
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            is_area = 0 <= nh < H and 0 <= nw < W
            if is_area and Fields[nh][nw] == "W" and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w] + 1
                Q.append((nh, nw))
    print(dist[gh][gw])


if __name__ == "__main__":
    main()
