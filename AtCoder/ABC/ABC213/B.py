def main():
    _ = int(input())
    A = list(map(int, input().split()))
    score = sorted([[v, i + 1] for i, v in enumerate(A)])
    print(score[-2][1])


if __name__ == "__main__":
    main()
