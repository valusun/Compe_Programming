def main():
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    cnt = 0
    while b > 0:
        cnt += a // b
        a %= b
        a, b = max(a, b), min(a, b)
    print(cnt - 1)


if __name__ == "__main__":
    main()
