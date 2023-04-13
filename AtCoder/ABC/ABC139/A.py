def main():
    S = list(input())
    T = list(input())
    print(sum([S[i] == T[i] for i in range(3)]))


if __name__ == "__main__":
    main()
