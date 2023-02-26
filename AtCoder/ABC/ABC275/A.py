def main():
    _ = int(input())
    A = list(map(int, input().split()))
    print(A.index(max(A)) + 1)


if __name__ == "__main__":
    main()
