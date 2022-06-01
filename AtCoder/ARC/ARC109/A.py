def main():
    a, b, x, y = map(int, input().split())
    if a > b:
        print(min((a - b - 1) * y + x, (a - b - 1) * 2 * x + x))
    else:
        print(min((b - a) * y + x, x + (b - a) * 2 * x))


if __name__ == "__main__":
    main()
