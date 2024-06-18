from bisect import bisect_right


def main():
    N, H, X = map(int, input().split())
    P = list(map(int, input().split()))
    if (X - H) in P:
        print(P.index(X - H) + 1)
    else:
        print(bisect_right(P, X - H) + 1)


if __name__ == "__main__":
    main()
