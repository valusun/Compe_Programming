def main():
    a, b = map(int, input().split())
    print("Yes" if a * 2 <= b <= a * 2 + 1 else "No")


if __name__ == "__main__":
    main()
