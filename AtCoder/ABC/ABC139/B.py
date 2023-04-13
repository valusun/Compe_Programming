def main():
    A, B = map(int, input().split())
    print(((B - A) + (A - 1) - 1) // (A - 1) + 1)


if __name__ == "__main__":
    main()
