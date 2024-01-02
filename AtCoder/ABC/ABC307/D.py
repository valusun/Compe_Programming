def main():
    N = int(input())
    S = input()
    memo = [0] * (N + 1)
    left = []
    for i, s in enumerate(S):
        if s == "(":
            left.append(i)
            continue
        if s == ")" and left:
            memo[left[-1]] += 1
            memo[i + 1] -= 1
            left.pop()
    for i in range(1, N):
        memo[i] += memo[i - 1]
    ans = [S[i] for i in range(N) if not memo[i]]
    print(*ans, sep="")


if __name__ == "__main__":
    main()
