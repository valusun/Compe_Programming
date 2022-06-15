def main():
    _ = map(int, input().split())
    S = list(input().split())
    T = set(list(input().split()))
    for s in S:
        if s in T:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
