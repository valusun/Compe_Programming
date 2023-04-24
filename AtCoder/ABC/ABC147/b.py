def main():
    S = input()
    n = len(S)
    cnt = 0
    for i in range(n // 2):
        cnt += S[i] != S[-i - 1]
    print(cnt)


if __name__ == "__main__":
    main()
