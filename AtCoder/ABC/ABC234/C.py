def main():
    K = int(input())
    ans = ""
    while K:
        if K % 2:
            ans += "2"
        else:
            ans += "0"
        K //= 2
    print(ans[::-1])


if __name__ == "__main__":
    main()
