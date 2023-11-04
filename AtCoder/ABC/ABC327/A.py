def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        if sorted([S[i - 1], S[i]]) == ["a", "b"]:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
