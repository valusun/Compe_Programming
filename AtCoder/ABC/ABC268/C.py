def main():
    N = int(input())
    A = list(map(int, input().split()))
    roll = [0] * N
    for i, d in enumerate(A):
        for j in range(-1, 2):
            roll[(i + j - d) % N] += 1
    print(max(roll))


if __name__ == "__main__":
    main()
