def main():
    _ = int(input())
    A = list(map(int, input().split()))
    counts = [0] * 9
    for a in A:
        counts[a - 1] += 1
    print(counts.index(max(counts)) + 1)


if __name__ == "__main__":
    main()
