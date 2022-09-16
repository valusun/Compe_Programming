def main():
    S = input()
    K = int(input())
    for i in range(min(len(S), K)):
        if S[i] != "1":
            print(S[i])
            break
    else:
        print(1)


if __name__ == "__main__":
    main()
