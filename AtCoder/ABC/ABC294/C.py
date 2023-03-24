import bisect


def main():
    _ = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted(A + B)

    def solve(X):
        ret = []
        for x in X:
            ret.append(bisect.bisect_left(C, x) + 1)
        print(*ret)

    solve(A)
    solve(B)


if __name__ == "__main__":
    main()
