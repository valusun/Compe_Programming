def main():
    S = input()
    K = int(input())
    cusum_S = [0]
    for s in S:
        if s == ".":
            cusum_S.append(cusum_S[-1] + 1)
        else:
            cusum_S.append(cusum_S[-1])
    ans = 0
    len_S = len(S)
    right = 0
    for left in range(len_S):
        while right < len_S and cusum_S[right + 1] - cusum_S[left] <= K:
            right += 1
        ans = max(ans, right - left)
    print(ans)


if __name__ == "__main__":
    main()
