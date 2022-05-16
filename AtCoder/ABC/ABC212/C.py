from bisect import bisect_left


def main():
    _, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ans = 10**9 + 7
    for a in A:
        idx = bisect_left(B, a) % M
        ans = min(ans, min(abs(a - B[idx - 1]), abs(a - B[idx])))
    print(ans)


if __name__ == "__main__":
    main()
