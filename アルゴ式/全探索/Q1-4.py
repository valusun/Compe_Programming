def main():
    N, V = map(int, input().split())
    A = list(map(int, input().split()))[::-1]
    print(N - A.index(V) - 1 if V in A else -1)


if __name__ == "__main__":
    main()
