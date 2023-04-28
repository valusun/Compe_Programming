def main():
    a, b, k = map(int, input().split())
    print(max(0, a - k), min(b, max(0, a + b - k)))


if __name__ == "__main__":
    main()
