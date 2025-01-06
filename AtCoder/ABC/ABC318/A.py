def main():
    N, M, P = map(int, input().split())
    print((N - M) // P + 1 if N >= P else 0)


if __name__ == "__main__":
    main()
