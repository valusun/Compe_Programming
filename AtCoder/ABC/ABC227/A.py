def main():
    N, K, A = map(int, input().split())
    print((K + A - 1) % N if (K + A - 1) % N else N)


if __name__ == "__main__":
    main()
