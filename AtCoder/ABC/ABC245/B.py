def main():
    N = int(input())
    A = set(list(map(int, input().split())))
    for i in range(N + 1):
        if i not in A:
            print(i)
            break


if __name__ == "__main__":
    main()
