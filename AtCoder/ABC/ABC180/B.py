from math import sqrt


def main():
    _ = int(input())
    X = list(map(int, input().split()))
    mn, yk, cb = 0, 0, 0
    for x in X:
        mn += abs(x)
        yk += abs(x) ** 2
        cb = max(cb, abs(x))
    print(mn, sqrt(yk), cb, sep="\n")


if __name__ == "__main__":
    main()
