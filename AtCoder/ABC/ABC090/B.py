def IsPalindrome(n):
    """回文か判定する"""
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[-1 - i]:
            return False
    return True


def main():
    A, B = map(int, input().split())
    ans = 0
    for n in range(A, B + 1):
        if IsPalindrome(n):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
