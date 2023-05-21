def main():
    H, W, K = map(int, input().split())
    ch = [list(input()) for _ in range(H)]
    ans = 10**18
    for i in range(2**H):
        is_ok = True
        cut_groups = [0] * H
        cut_cnt = 0
        for j in range(H - 1):
            if i & (1 << j):
                cut_groups[j + 1] = cut_groups[j] + 1
                cut_cnt += 1
            else:
                cut_groups[j + 1] = cut_groups[j]
        add = 0
        bef = [0] * (cut_cnt + 1)  # 横方向に切らないパターンがあるため
        for w in range(W):
            now = [0] * (cut_cnt + 1)
            is_cutting = False
            for h in range(H):
                bef[cut_groups[h]] += int(ch[h][w])
                now[cut_groups[h]] += int(ch[h][w])
                if now[cut_groups[h]] > K:
                    is_ok = False
                if bef[cut_groups[h]] > K:
                    is_cutting = True
            if is_cutting:
                add += 1
                bef = now  # wのループ後に新しくnowを作っているので参照でOK
        if is_ok:
            ans = min(ans, cut_cnt + add)
    print(ans)


if __name__ == "__main__":
    main()
