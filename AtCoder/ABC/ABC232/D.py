from collections import deque


def main():
    H, W = map(int, input().split())
    Field = [list(input()) for _ in range(H)]
    Field[0][0] = "#"
    ans = 1
    que = deque()
    que.append((0, 0, 1))
    while que:
        h, w, d = que.popleft()
        for dh, dw in ((0, 1), (1, 0)):
            next_h = h + dh
            next_w = w + dw
            if 0 <= next_h < H and 0 <= next_w < W and Field[next_h][next_w] == ".":
                ans = max(ans, d + 1)
                Field[next_h][next_w] = "#"
                que.append((next_h, next_w, d + 1))
    print(ans)


if __name__ == "__main__":
    main()
