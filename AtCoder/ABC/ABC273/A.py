def main():
    def func(n):
        if n == 0:
            return 1
        return n * func(n - 1)

    print(func(int(input())))


if __name__ == "__main__":
    main()
