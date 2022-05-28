def main():
    N = int(input())
    for i in range(1, 40):
        for j in range(1, 40):
            if (tmp := 3**i + 5**j) == N:
                print(i, j)
                exit()
            if tmp > N:
                break
    print(-1)


if __name__ == "__main__":
    main()
