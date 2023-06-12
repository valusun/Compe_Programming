def main():
    N = int(input())
    ans = ""
    while N != 0:
        N -= 1
        n = N % 26
        ans += chr(ord("a") + n)
        N //= 26
    print(ans[::-1])


if __name__ == "__main__":
    main()
