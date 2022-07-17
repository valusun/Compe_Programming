def main():
    N = int(input())
    A = list(map(int, input().split()))

    even_positive_cnt = 0
    now_sum = 0

    for i in range(N):
        if i % 2 == 0:
            if now_sum + A[i] <= 0:
                even_positive_cnt += 1 - (now_sum + A[i])
                now_sum = 1
            else:
                now_sum += A[i]
        else:
            if now_sum + A[i] >= 0:
                even_positive_cnt += 1 + (now_sum + A[i])
                now_sum = -1
            else:
                now_sum += A[i]

    even_negative_cnt = 0
    now_sum = 0

    for i in range(N):
        if i % 2 == 0:
            if now_sum + A[i] >= 0:
                even_negative_cnt += 1 + (now_sum + A[i])
                now_sum = -1
            else:
                now_sum += A[i]
        else:
            if now_sum + A[i] <= 0:
                even_negative_cnt += 1 - (now_sum + A[i])
                now_sum = 1
            else:
                now_sum += A[i]

    print(min(even_positive_cnt, even_negative_cnt))


if __name__ == "__main__":
    main()
