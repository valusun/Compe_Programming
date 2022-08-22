def main():
    _ = int(input())
    A = set(list(input().split()))
    print("Three" if len(A) == 3 else "Four")


if __name__ == "__main__":
    main()
