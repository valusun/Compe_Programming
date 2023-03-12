def main():
    N = int(input())
    S = input()
    T = input()
    print(sum([1 for i in range(N) if S[i] != T[i]]))


if __name__ == "__main__":
    main()
