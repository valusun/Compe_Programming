def main():
    _ = int(input())
    S = input()
    print("Yes" if S.count("o") and not S.count("x") else "No")


if __name__ == "__main__":
    main()
