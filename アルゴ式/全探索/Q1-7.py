def main():
    _ = int(input())
    A = list(map(int, input().split()))
    print(A.index(max(A)))


if __name__ == "__main__":
    main()
