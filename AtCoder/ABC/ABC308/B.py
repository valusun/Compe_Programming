def main():
    N, M = map(int, input().split())
    C = list(input().split())
    D = list(input().split())
    P = list(map(int, input().split()))
    memo = dict()
    for i, d in enumerate(D):
        memo[d] = P[i + 1]
    ans = 0
    for c in C:
        ans += memo[c] if c in memo else P[0]
    print(ans)


if __name__ == "__main__":
    main()
