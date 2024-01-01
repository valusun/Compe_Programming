def main():
    N = int(input())
    print(5 * (N // 5) + 5 if N % 10 % 5 >= 3 else 5 * (N // 5))


if __name__ == "__main__":
    main()
