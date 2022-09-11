def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    changed_cnt = N - A.count(min(A))
    if changed_cnt == 0:
        print(0)
    elif changed_cnt < K:
        print(1)
    else:
        print((changed_cnt + K - 2) // (K - 1))


if __name__ == "__main__":
    main()
