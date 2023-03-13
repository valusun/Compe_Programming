def main():
    _ = int(input())
    S = input()
    ans = 0
    for i, s1 in enumerate(S):
        for s2 in S[i + 1 :]:
            if s1 == s2:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
