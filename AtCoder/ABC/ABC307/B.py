def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            s1 = S[i] + S[j]
            s2 = S[j] + S[i]
            if s1 == s1[::-1] or s2 == s2[::-1]:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
