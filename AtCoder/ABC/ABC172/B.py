def main():
    S = input()
    T = input()
    ans = sum([1 for i in range(len(S)) if S[i] != T[i]])
    print(ans)


if __name__ == "__main__":
    main()
