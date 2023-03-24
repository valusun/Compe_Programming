def main():
    _ = int(input())
    A = list(map(int, input().split()))
    print(*[a for a in A if a % 2 == 0])


if __name__ == "__main__":
    main()
