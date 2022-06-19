def ceil(x, y):
    return (x + (y - 1)) // y


def main():
    N = int(input())
    ratios = [list(map(int, input().split())) for _ in range(N)]
    votes = ratios[0]
    for a, t in ratios[1:]:
        n = max(ceil(votes[0], a), ceil(votes[1], t))
        votes = [a * n, t * n]
    print(sum(votes))


if __name__ == "__main__":
    main()
