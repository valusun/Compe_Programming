def main():
    n = input()
    ans = ["1" if s == "9" else "9" for s in n]
    print(*ans, sep="")


if __name__ == "__main__":
    main()
