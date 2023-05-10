from itertools import accumulate


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = [(p + 1) / 2 for p in P]
    S = [0] + list(accumulate(S))
    ans = 0
    for k in range(K, N + 1):
        ans = max(ans, S[k] - S[k - K])
    print(ans)


if __name__ == "__main__":
    main()
