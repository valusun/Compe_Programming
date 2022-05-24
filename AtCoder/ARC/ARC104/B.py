def main():
    N, S = input().split()
    N = int(N)
    ans = 0
    for i in range(N):
        A, T, C, G = 0, 0, 0, 0
        for j in range(i, N):
            if S[j] == "A":
                A += 1
            elif S[j] == "T":
                T += 1
            elif S[j] == "C":
                C += 1
            else:
                G += 1
        if A - T == C - G == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
