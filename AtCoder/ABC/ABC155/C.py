from collections import Counter


def main():
    N = int(input())
    c = Counter()
    for _ in range(N):
        c[input()] += 1
    mx = c.most_common()[0][1]
    k = [s for s, x in c.most_common() if x == mx]
    print(*sorted(k), sep="\n")


if __name__ == "__main__":
    main()
