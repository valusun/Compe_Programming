def main():
    a, b = map(int, input().split())
    c = a - b
    print(c * (c - 1) // 2 - b)


if __name__ == "__main__":
    main()
