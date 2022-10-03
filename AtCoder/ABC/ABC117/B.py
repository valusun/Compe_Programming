def main():
    _ = int(input())
    L = list(map(int, input().split()))
    print("Yes" if max(L) < sum(L) - max(L) else "No")


if __name__ == "__main__":
    main()
