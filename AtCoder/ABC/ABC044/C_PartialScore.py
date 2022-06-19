def main():
    N, A = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(1, 2**N):
        score, choose_cnt = 0, 0
        for j in range(N):
            if i & (1 << j):
                score += X[j]
                choose_cnt += 1
        if score / choose_cnt == A:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
