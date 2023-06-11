from bisect import bisect_right


def main():
    N, D, A = map(int, input().split())
    monsters = sorted([list(map(int, input().split())) for _ in range(N)])
    places, hps = [], []
    for p, h in monsters:
        places.append(p)
        hps.append(h)
    exploded_cnts = [0] * (N + 1)
    ans = 0
    for i in range(N):
        hps[i] -= exploded_cnts[i] * A
        if hps[i] > 0:
            mx_rng = places[i] + (D * 2)
            bom_cnt = (hps[i] + A - 1) // A
            idx = bisect_right(places, mx_rng)
            exploded_cnts[i] += bom_cnt
            exploded_cnts[idx] -= bom_cnt
            ans += bom_cnt
        exploded_cnts[i + 1] += exploded_cnts[i]
    print(ans)


if __name__ == "__main__":
    main()
