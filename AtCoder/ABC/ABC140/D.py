def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(1, N):
        cnt += S[i - 1] != S[i]
    print(N - 1 - max(cnt - 2 * K, 0))


if __name__ == "__main__":
    main()
