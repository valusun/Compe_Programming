def main():
    N = int(input())
    t = N // 500
    print(t * 1000 + (N - 500 * t) // 5 * 5)


if __name__ == "__main__":
    main()
