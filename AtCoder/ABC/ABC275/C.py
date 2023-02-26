def Judge(coords):
    for c in coords:
        if not (c % 1 == 0 and 0 <= c < 9):
            return False
    return True


def main():
    S = [list(input()) for _ in range(9)]
    pair = []
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                pair.append((i, j))
    pair_cnt = len(pair)

    ans = 0
    for i in range(pair_cnt):
        for j in range(i + 1, pair_cnt):
            ax, ay = pair[i]
            bx, by = pair[j]
            mx, my = (ax + bx) / 2, (ay + by) / 2  # 中点
            cx, cy = mx - (ay - my), my + (ax - mx)
            dx, dy = mx + (ay - my), my - (ax - mx)
            if Judge([cx, cy, dx, dy]):
                cx, cy, dx, dy = map(int, [cx, cy, dx, dy])
                if S[cx][cy] == S[dx][dy] == "#":
                    ans += 1
    print(ans // 2)  # 同じ正方形を数えるため


if __name__ == "__main__":
    main()
