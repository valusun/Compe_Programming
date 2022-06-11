def main():
    X, Y = map(int, input().split())
    print(max(0, (Y - X + 9) // 10))


if __name__ == "__main__":
    main()
