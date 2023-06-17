def main():
    _ = int(input())
    S = input()
    ss = [x * 2 for x in S]
    print(*ss, sep="")


if __name__ == "__main__":
    main()
