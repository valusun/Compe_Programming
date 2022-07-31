def main():
    X, t = map(int, input().split())
    print(max(0, X - t))


if __name__ == "__main__":
    main()
