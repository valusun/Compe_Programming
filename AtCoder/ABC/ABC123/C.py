def main():
    N = int(input())
    A = [int(input()) for _ in range(5)]
    print(4 + ((N + min(A) - 1) // min(A)))


if __name__ == "__main__":
    main()
