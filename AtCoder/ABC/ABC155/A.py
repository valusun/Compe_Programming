def main():
    a, b, c = map(int, input().split())
    print("Yes" if a == b != c or a != b == c or a == c != b else "No")


if __name__ == "__main__":
    main()
