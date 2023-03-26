from collections import defaultdict


def main():
    S = input()
    cnt = [0] * 10
    d = defaultdict(int)  # 偶奇の盤面を保持する
    d["".join(str(c) for c in cnt)] += 1
    for s in S:
        cnt[int(s)] = 1 if (cnt[int(s)] + 1) % 2 else 0
        d["".join([str(c) for c in cnt])] += 1
    ans = 0
    for _, c in d.items():
        ans += c * (c - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
