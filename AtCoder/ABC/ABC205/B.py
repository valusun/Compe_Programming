def main():
    N = int(input())
    if len(set(list(range(1, N + 1))) - set(list(map(int, input().split())))):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
