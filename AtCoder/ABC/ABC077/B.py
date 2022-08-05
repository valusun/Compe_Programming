def main():
    N = int(input())
    now = 0
    while (now + 1) ** 2 <= N:
        now += 1
    print(now**2)


if __name__ == "__main__":
    main()
