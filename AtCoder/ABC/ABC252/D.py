def main():
    N = int(input())
    A = list(map(int, input().split()))

    LIMIT = 2 * 10**5
    LIMIT = max(A)
    cnt = [0] * (LIMIT + 1)
    for v in A:
        cnt[v] += 1

    # 全パターン
    ans = N * (N - 1) * (N - 2) // 6
    for v in cnt:
        # 種類数が2個
        ans -= v * (v - 1) // 2 * (N - v)
        # 種類数が1個
        ans -= v * (v - 1) * (v - 2) // 6

    print(ans)


if __name__ == "__main__":
    main()
