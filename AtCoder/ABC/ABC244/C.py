def main():
    N = int(input())
    Used = [0] * (2 * N + 2)
    Used[0] = 1
    while True:
        for j in range(2 * N + 2):
            if Used[j]:
                continue
            print(j, flush=True)
            Used[j] = 1
            x = int(input())
            Used[x] = 1
            if x == 0:
                exit()


if __name__ == "__main__":
    main()
