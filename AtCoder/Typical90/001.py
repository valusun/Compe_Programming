def main():
    N, L = map(int, input().split())
    K = int(input())
    A = [0] + list(map(int, input().split()))
    A.append(L)

    ok = -1
    ng = 10**9
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        now = 0
        cut_cnt = 0
        for i in range(N + 1):
            if now + (A[i + 1] - A[i]) >= mid and K != cut_cnt:
                now = 0
                cut_cnt += 1
            else:
                now += A[i + 1] - A[i]
        if mid <= now:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
