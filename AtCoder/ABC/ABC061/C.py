def main():
    N, K = map(int, input().split())
    inserted_numbers = [0] * (10**5 + 1)
    for _ in range(N):
        a, b = map(int, input().split())
        inserted_numbers[a] += b
    seen = 0
    for i, v in enumerate(inserted_numbers):
        if seen + v >= K:
            print(i)
            break
        seen += v


if __name__ == "__main__":
    main()
