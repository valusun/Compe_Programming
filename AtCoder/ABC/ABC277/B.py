def main():
    N = int(input())
    seen = set()
    for _ in range(N):
        S = input()
        is_no = S[0] not in "HDCS" or S[1] not in "A23456789TJQK"
        if S in seen or is_no:
            print("No")
            exit()
        seen.add(S)
    print("Yes")


if __name__ == "__main__":
    main()
