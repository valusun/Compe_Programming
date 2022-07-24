def main():
    N, A, B = map(int, input().split())
    enemy = [int(input()) for _ in range(N)]
    C = A - B

    def IsDefeat(x):
        cnt = 0
        for h in enemy:
            remaining_amount = h - (x * B)
            if remaining_amount > 0:
                cnt += (remaining_amount + C - 1) // C
        if cnt <= x:
            return True
        return False

    ok = 10**18
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if IsDefeat(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
