def main():
    N, K = map(int, input().split())
    mod = [0] * K
    for i in range(1, N + 1):
        mod[i % K] += 1

    ans = 0
    for a in range(K):
        b = (K - a) % K
        c = (K - a) % K
        if (b + c) % K == 0:
            ans += mod[a] * mod[b] * mod[c]
    print(ans)


if __name__ == "__main__":
    main()
