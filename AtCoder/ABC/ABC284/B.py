def main():
    N = int(input())
    for _ in range(N):
        n = int(input())
        A = list(map(int, input().split()))
        print(sum([1 for i in A if i % 2 == 1]))


if __name__ == "__main__":
    main()
