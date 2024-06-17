def main():
    _ = int(input())
    D = list(map(int, input().split()))
    middle = (sum(D) + 1) // 2
    for i, d in enumerate(D):
        if d >= middle:
            print(i + 1, middle)
            exit()
        middle -= d


if __name__ == "__main__":
    main()
