def main():
    k = 0
    N = int(input())
    while 2 ** (k + 1) <= N:
        k += 1
    print(k)


if __name__ == "__main__":
    main()
