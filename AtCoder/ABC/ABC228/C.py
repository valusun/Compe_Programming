def main():
    N, K = map(int, input().split())
    Points = [sum(list(map(int, input().split()))) for _ in range(N)]
    reference_point = sorted(Points, reverse=True)[K - 1]
    for p in Points:
        print("Yes" if p + 300 >= reference_point else "No")


if __name__ == "__main__":
    main()
