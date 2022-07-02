def main():
    N, M = map(int, input().split())
    if N >= M // 2:
        print(M // 2)
    else:
        print(N + (M - N * 2) // 4)


if __name__ == "__main__":
    main()
