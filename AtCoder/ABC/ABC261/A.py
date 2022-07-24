def main():
    a, b, c, d = map(int, input().split())
    print(max(0, min(b, d) - max(a, c)))


if __name__ == "__main__":
    main()
