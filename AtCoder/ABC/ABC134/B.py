def main():
    N, D = map(int, input().split())
    b = D * 2 + 1
    print(-(-N // b))


if __name__ == "__main__":
    main()
