def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))

    positive, negative = [0], [0]
    for num in A:
        positive.append(num) if num > 0 else negative.append(abs(num))
    negative = sorted(negative)

    positive_size = len(positive)
    negative_size = len(negative)

    ans = float("inf")
    for p in range(positive_size):
        n = K - p
        if 0 <= n and n < negative_size:
            ans = min(ans, positive[p] * 2 + negative[n])
    for n in range(negative_size):
        p = K - n
        if 0 <= p and p < positive_size:
            ans = min(ans, negative[n] * 2 + positive[p])
    print(ans)


if __name__ == "__main__":
    main()
