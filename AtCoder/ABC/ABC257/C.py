from bisect import bisect_left


def main():
    _ = int(input())
    S = input()
    W = list(map(int, input().split())) + [0]
    a, c = [], []
    for i, s in enumerate(S):
        if s == "0":
            c.append(W[i])
        else:
            a.append(W[i])
    c, a, W = sorted(c), sorted(a), sorted(W)
    ans = 0

    def Check(c, a, w, ans):
        x = bisect_left(c, w)
        y = bisect_left(a, w)
        return max(ans, x + (len(a) - y))

    for w in W:
        ans = Check(c, a, w, ans)
        ans = Check(c, a, w + 1, ans)
    print(ans)


if __name__ == "__main__":
    main()
