def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    knowing = [False] * N
    knowing_cnt = 0
    while not knowing[X - 1]:
        knowing[X - 1] = True
        knowing_cnt += 1
        X = A[X - 1]
    print(knowing_cnt)


if __name__ == "__main__":
    main()
