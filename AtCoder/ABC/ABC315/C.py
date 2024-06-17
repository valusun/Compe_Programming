from collections import Counter


def main():
    N = int(input())
    ices = [list(map(int, input().split())) for _ in range(N)]
    kind_to_max = Counter()
    for f, s in ices:
        if f not in kind_to_max or s > kind_to_max[f]:
            kind_to_max[f] = s
            continue
    # 最大の掛け合わせ
    ices.sort(key=lambda x: x[1], reverse=True)
    t1, t2 = ices[0], ices[1]
    p1 = t1[1] + t2[1] if t1[0] != t2[0] else t1[1] + t2[1] // 2
    # 種類を考慮
    if len(kind_to_max) >= 2:
        t3, t4 = kind_to_max.most_common(2)
        p2 = t3[1] + t4[1]
    else:
        p2 = 0
    print(max(p1, p2))


if __name__ == "__main__":
    main()
