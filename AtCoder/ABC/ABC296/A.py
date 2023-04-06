def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        if S[i - 1] == S[i]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
