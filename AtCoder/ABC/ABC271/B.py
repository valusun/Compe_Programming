def main():
    N, Q = map(int, input().split())
    sequences = [list(map(int, input().split()))[1:] for _ in range(N)]
    for _ in range(Q):
        s, t = map(int, input().split())
        print(sequences[s - 1][t - 1])


if __name__ == "__main__":
    main()
