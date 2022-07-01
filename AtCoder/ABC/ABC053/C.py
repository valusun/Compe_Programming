def main():
    x = int(input())
    cnt = x // 11 * 2
    x %= 11
    if not x:
        print(cnt)
    elif x <= 6:
        print(cnt + 1)
    else:
        print(cnt + 2)


if __name__ == "__main__":
    main()
