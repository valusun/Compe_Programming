def main():
    P = list(map(int, input().split()))
    for p in P:
        print(chr(p + 96), end="")


if __name__ == "__main__":
    main()
