from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    c = Counter()
    for a in A:
        c[a] += 1
    ans = 0
    for i, v in c.items():
        if i == v:
            continue
        elif i > v:
            ans += v
        else:
            ans += v - i
    print(ans)


if __name__ == "__main__":
    main()
