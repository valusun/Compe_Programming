def main():
    N = int(input())
    for i in range(5):
        if (N + i) % 4 == 2:
            print(N + i)
            break


if __name__ == "__main__":
    main()
