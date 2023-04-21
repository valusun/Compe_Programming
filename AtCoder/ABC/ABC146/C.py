def calc(a, b, d):
    return a * d + b * len(str(d))


def main():
    A, B, X = map(int, input().split())
    ok = 0
    ng = 10**9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if calc(A, B, mid) <= X:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
