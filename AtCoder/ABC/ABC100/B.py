def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(100**D * N)


if __name__ == "__main__":
    main()
