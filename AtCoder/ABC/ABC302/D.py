import bisect


def main():
    _, _, D = map(int, input().split())
    A = sorted(list(set(map(int, input().split()))))
    B = sorted(list(set(map(int, input().split()))))
    ans = -1
    for a in A:
        idx = bisect.bisect_right(B, a + D)
        if idx == 0:
            idx = 1
        if abs(a - B[idx - 1]) > D:
            continue
        ans = max(ans, a + B[idx - 1])
    print(ans)


if __name__ == "__main__":
    main()
