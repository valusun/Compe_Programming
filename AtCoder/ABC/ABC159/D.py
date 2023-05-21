from collections import Counter


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    c = Counter()
    for a in A:
        c[a] += 1
    s = 0
    for _, v in c.items():
        s += v * (v - 1) // 2
    for a in A:
        v = c[a]
        print(s - v * (v - 1) // 2 + (v - 1) * (v - 2) // 2)


if __name__ == "__main__":
    main()
