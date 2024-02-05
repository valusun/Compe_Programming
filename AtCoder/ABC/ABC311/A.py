def main():
    _ = int(input())
    S = input()
    print(max(*map(lambda x: S.index(x), ["A", "B", "C"])) + 1)


if __name__ == "__main__":
    main()
