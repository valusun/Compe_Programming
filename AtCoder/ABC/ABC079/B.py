def main():
    N = int(input())
    Lucas = [2, 1]
    for _ in range(N):
        Lucas.append(Lucas[-2] + Lucas[-1])
    print(Lucas[N])


if __name__ == "__main__":
    main()
