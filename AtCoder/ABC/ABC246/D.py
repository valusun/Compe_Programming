def CalculateEquation(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


def main():
    N = int(input())
    X = 10**18 + 1
    for a in range(10**6 + 1):
        ok = 10**6 + 1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if CalculateEquation(a, mid) >= N:
                ok = mid
            else:
                ng = mid
        X = min(X, CalculateEquation(a, ok))
    print(X)


if __name__ == "__main__":
    main()
