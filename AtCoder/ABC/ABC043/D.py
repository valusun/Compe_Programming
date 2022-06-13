def main():
    S = input()
    for i in range(1, len(S)):
        if S[i - 1] == S[i]:
            print(i, i + 1)
            break
        elif i > 1 and S[i - 2] == S[i]:
            print(i - 1, i + 1)
            break
    else:
        print(-1, -1)


if __name__ == "__main__":
    main()
