def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = []
    for i in range(N):
        old_alfabet = ""
        for s in S[i]:
            for j in range(26):
                if s == X[j]:
                    old_alfabet += chr(j + 97)
                    break
        S1.append([old_alfabet, S[i]])
    S1.sort()
    for s in S1:
        print(s[1])


if __name__ == "__main__":
    main()
