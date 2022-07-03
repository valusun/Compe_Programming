def main():
    A, B, C = map(int, input().split())
    print("Yes" if B == sorted([A, B, C])[1] else "No")


if __name__ == "__main__":
    main()
