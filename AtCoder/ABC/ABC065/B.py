def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    buttons = [False] * N
    lamp = 0
    cnt = 0
    while not buttons[lamp]:
        buttons[lamp] = True
        lamp = A[lamp] - 1
        cnt += 1
        if lamp == 1:
            print(cnt)
            break
    else:
        print("-1")


if __name__ == "__main__":
    main()
