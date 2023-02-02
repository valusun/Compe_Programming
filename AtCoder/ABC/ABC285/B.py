def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        cnt = 0
        for j in range(N):
            if i + j == N:
                break
            if S[j] == S[i + j]:
                break
            cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
