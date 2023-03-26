from collections import defaultdict


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    ans = 0
    for a in A:
        d[a] += 1
        if d[a] % 2 == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
