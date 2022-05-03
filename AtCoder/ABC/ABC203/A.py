def main():
    a, b, c = sorted(map(int, input().split()))
    if a != b != c:
        print(0)
    elif a == b:
        print(c)
    elif b == c:
        print(a)


if __name__ == "__main__":
    main()
