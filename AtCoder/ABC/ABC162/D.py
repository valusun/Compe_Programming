def main():
    N = int(input())
    S = input()
    r, g, b = 0, 0, 0
    for s in S:
        r += 1 if s == "R" else 0
        g += 1 if s == "G" else 0
        b += 1 if s == "B" else 0
    ans = r * g * b
    for i in range(N):
        for j in range(i + 1, N):
            if (k := j + (j - i)) >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
