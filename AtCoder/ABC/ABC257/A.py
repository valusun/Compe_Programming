def main():
    N, X = map(int, input().split())
    print(chr((X - 1) // N + 65))


if __name__ == "__main__":
    main()
