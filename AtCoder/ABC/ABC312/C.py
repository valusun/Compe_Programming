from bisect import bisect_left, bisect_right


def main():
    _ = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ng = -1
    ok = max(max(A) + 1, max(B) + 1)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        seller = bisect_right(A, mid)
        buyer = len(B) - bisect_left(B, mid)
        if seller >= buyer:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
