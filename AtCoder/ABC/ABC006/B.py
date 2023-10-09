def main():
    N = int(input())
    seq = [0, 0, 1]
    for n in range(3, N):
        seq.append((seq[n - 3] + seq[n - 2] + seq[n - 1]) % 10007)
    print(seq[N - 1])


if __name__ == "__main__":
    main()
