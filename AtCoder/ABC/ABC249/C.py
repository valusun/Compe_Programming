def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1, 2**N):
        alphabet_counts = [0] * 26
        for j in range(N):
            if i & (1 << j):
                for k in S[j]:
                    alphabet_counts[ord(k) - 97] += 1
        ans = max(ans, alphabet_counts.count(K))
    print(ans)


if __name__ == "__main__":
    main()
