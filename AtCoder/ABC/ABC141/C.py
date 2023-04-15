def main():
    N, K, Q = map(int, input().split())
    A = list(int(input()) for _ in range(Q))
    correct = [0] * N
    for a in A:
        correct[a - 1] += 1
    ng_line = Q - K
    for i, c in enumerate(correct):
        print("Yes" if c > ng_line else "No")


if __name__ == "__main__":
    main()
