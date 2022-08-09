from collections import Counter


def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    c = Counter()
    for a in A:
        c[a] += 1
    ans = 0
    for _, v in list(c.most_common())[K:]:
        ans += v
    print(ans)


if __name__ == "__main__":
    main()
