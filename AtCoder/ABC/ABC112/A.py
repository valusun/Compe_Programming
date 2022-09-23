def main():
    N = int(input())
    if N == 1:
        print("Hello World")
    else:
        print(sum(list(int(input()) for _ in range(2))))


if __name__ == "__main__":
    main()
