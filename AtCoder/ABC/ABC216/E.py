def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ok, ng = 2 * 10**9 + 1, 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        ride_cnt = [a - mid + 1 for a in A if a >= mid]
        if sum(ride_cnt) <= K:
            ok = mid
        else:
            ng = mid

    amount = K
    ans = 0
    for a in A:
        if a >= ok:
            diff = a - ok + 1
            ans += diff * (a + ok) // 2
            amount -= diff
    ans += amount * (ok - 1)
    print(ans)


if __name__ == "__main__":
    main()
