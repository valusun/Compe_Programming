def main():
    X, Y = map(int, input().split("."))
    print(X + 1 if Y >= 500 else X)


if __name__ == "__main__":
    main()
