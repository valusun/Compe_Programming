def main():
    S = input()
    K = int(input())
    n = len(S)
    substring = set()
    for i in range(n):
        for j in range(i + 1, min(n + 1, i + K + 1)):
            substring.add(S[i:j])
    print(sorted(list(substring))[K - 1])


if __name__ == "__main__":
    main()
