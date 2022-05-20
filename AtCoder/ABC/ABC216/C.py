def main():
    N = int(input())
    ans = ""
    while N:
        if N % 2:
            N -= 1
            ans += "A"
        else:
            N //= 2
            ans += "B"
    print(ans[::-1])


if __name__ == "__main__":
    main()
