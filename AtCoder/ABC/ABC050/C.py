def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    elements_count = [0] * N
    for a in A:
        elements_count[a] += 1

    ans = 0
    for v in elements_count[1:]:
        if v != 0 and v != 2:
            break
    else:
        if N % 2 == 0 or (N % 2 and elements_count[0] == 1):
            ans = (2 ** (N // 2)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
