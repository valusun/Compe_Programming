def main():
    S = sorted(list(input()))
    if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
