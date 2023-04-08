def main():
    _ = int(input())
    print(1 / sum([1 / x for x in list(map(int, input().split()))]))


if __name__ == "__main__":
    main()
