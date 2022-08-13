def main():
    N = int(input())
    C, S, F = [], [], []
    for _ in range(N - 1):
        c, s, f = map(int, input().split())
        C.append(c)
        S.append(s)
        F.append(f)

    for i in range(N):
        now = 0
        for j in range(i, N - 1):
            if now < S[j]:
                now = S[j]
            elif now % F[j]:
                now = now + F[j] - now % F[j]
            now += C[j]
        print(now)


if __name__ == "__main__":
    main()
