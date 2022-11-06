from collections import deque


def main():
    def GetStart():
        for h in range(H):
            for w in range(W):
                if fields[h][w] == "S":
                    return h, w

    def Initialize():
        for i in range(4):
            th = start_h + dh[i]
            tw = start_w + dw[i]
            if 0 <= th < H and 0 <= tw < W:
                is_visited[th][tw] = False

    def IsCheck():
        cnt = 0
        for i in range(4):
            th = start_h + dh[i]
            tw = start_w + dw[i]
            if 0 <= th < H and 0 <= tw < W and is_visited[th][tw]:
                cnt += 1
        return cnt > 1

    H, W = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    dh = [0, 1, 0, -1]
    dw = [1, 0, -1, 0]
    start_h, start_w = GetStart()
    is_visited = [[False] * W for _ in range(H)]
    is_visited[start_h][start_w] = True
    for i in range(4):
        Initialize()
        sh, sw = start_h + dh[i], start_w + dw[i]
        Q = deque()
        Q.append((sh, sw))
        while Q:
            h, w = Q.popleft()
            for i in range(4):
                nh = h + dh[i]
                nw = w + dw[i]
                if 0 <= nh < H and 0 <= nw < W and fields[nh][nw] == ".":
                    if is_visited[nh][nw]:
                        continue
                    is_visited[nh][nw] = True
                    Q.append((nh, nw))
        if IsCheck():
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
