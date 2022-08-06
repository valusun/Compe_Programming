def main():
    N, M = map(int, input().split())
    once_time = 1900 * M + 100 * (N - M)
    expected_value = 2**M
    print(once_time * expected_value)


if __name__ == "__main__":
    main()
