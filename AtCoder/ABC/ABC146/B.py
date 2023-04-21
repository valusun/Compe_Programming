def main():
    N = int(input())
    S = input()
    base = ord("A")
    ans = [chr((ord(s) - base + N) % 26 + base) for s in S]
    print(*ans, sep="")


if __name__ == "__main__":
    main()
