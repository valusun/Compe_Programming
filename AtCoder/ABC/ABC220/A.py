def main():
    A, B, C = map(int, input().split())
    d = B // C * C
    print(d if A <= d else -1)


if __name__ == "__main__":
    main()
