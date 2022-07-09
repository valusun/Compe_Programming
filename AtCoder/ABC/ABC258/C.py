def main():
    N, Q = map(int, input().split())
    S = input()
    taken_out_cnt = 0
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            taken_out_cnt = (taken_out_cnt + x) % N
        else:
            print(S[x - taken_out_cnt - 1])


if __name__ == "__main__":
    main()
