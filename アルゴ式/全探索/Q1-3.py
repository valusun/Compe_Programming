def main():
    _ = int(input())
    A = list(map(int, input().split()))
    print(sum([1 for a in A if a > 0]))


if __name__ == "__main__":
    main()
