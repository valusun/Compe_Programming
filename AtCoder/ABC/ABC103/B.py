def main():
    S = input()
    T = input()
    for _ in range(len(S)):
        if S == T:
            print("Yes")
            break
        S = S[-1] + S[:-1]
    else:
        print("No")


if __name__ == "__main__":
    main()
