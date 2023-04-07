from collections import defaultdict


def main():
    N = int(input())
    c = defaultdict(int)
    for _ in range(N):
        s = sorted(input())
        c["".join(s)] += 1
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
