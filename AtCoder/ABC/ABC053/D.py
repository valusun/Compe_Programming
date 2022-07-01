def main():
    N = int(input())
    A = list(map(int, input().split()))
    number_kind_cnt = len(set(A))
    print(number_kind_cnt - 1 if (N - number_kind_cnt) % 2 else number_kind_cnt)


if __name__ == "__main__":
    main()
