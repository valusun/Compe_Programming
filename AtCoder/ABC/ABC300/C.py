def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    ans = [0] * min(H, W)

    # fmt: off
    def is_center(i, j):
        is_area = 0 <= i - 1 < H and 0 <= i + 1 < H and 0 <= j - 1 < W and 0 <= j + 1 < W
        if is_area and C[i - 1][j - 1] == C[i - 1][j + 1] == C[i + 1][j - 1] == C[i + 1][j + 1] == "#":
            return True
        return False
    # fmt:on

    def get_size(ci, cj, s):
        is_area = 0 <= ci - s < H and 0 <= ci + s < H and 0 <= cj - s < W and 0 <= cj + s < W
        if is_area:
            for i, j in ((ci - s, cj - s), (ci - s, cj + s), (ci + s, cj - s), (ci + s, cj + s)):
                if C[i][j] == ".":
                    return s - 1
            return get_size(ci, cj, s + 1)
        return s - 1

    for i in range(H):
        for j in range(W):
            if C[i][j] == ".":
                continue
            if is_center(i, j):
                ans[get_size(i, j, 1) - 1] += 1
    print(*ans)


if __name__ == "__main__":
    main()
