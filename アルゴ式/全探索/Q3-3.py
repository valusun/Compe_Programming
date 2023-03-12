def main():
    S = input()
    print(sum([1 for i in range(1, len(S)) if S[i] == S[i - 1]]))


if __name__ == "__main__":
    main()
