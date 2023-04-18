def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ab = L[i] + L[j]
            ok = -1
            ng = N
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if L[mid] < ab:
                    ok = mid
                else:
                    ng = mid
            ans += max(0, ok - j)
    print(ans)


if __name__ == "__main__":
    main()
