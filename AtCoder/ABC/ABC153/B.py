def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if sum(A) >= H else "No")


if __name__ == "__main__":
    main()
