def main():
    N, Q = map(int, input().split())
    S = input()
    num = [0] * N
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            num[i] = num[i - 1] + 1
        else:
            num[i] = num[i - 1]

    for _ in range(Q):
        left, right = map(int, input().split())
        print(num[right - 1] - num[left - 1])


if __name__ == "__main__":
    main()
