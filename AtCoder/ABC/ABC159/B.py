def IsPalindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def main():
    S = input()
    h = len(S) // 2
    print("Yes" if IsPalindrome(S) and IsPalindrome(S[:h]) and IsPalindrome(S[h + 1 :]) else "No")


if __name__ == "__main__":
    main()
