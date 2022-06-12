def main():
    N, _ = input().split()
    D = set(list(input().split()))
    while set(N) & D:
        N = str(int(N) + 1)
    print(N)


if __name__ == "__main__":
    main()
