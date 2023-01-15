def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    expected_values = [q / p for p, q in A]
    print(sum(expected_values))


if __name__ == "__main__":
    main()
