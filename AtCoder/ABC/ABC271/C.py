def main():
    N = int(input())
    A = list(map(int, input().split()))
    books = set(A)
    rem = N
    now = 0
    while rem > 0:
        if now + 1 in books:
            now += 1
            rem -= 1
        else:
            if rem >= 2:
                now += 1
                rem -= 2
            else:
                rem -= 1
    print(now)


if __name__ == "__main__":
    main()
