def main():
    N, A, B = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    print("Yes" if S[A][B] == "o" else "No")


if __name__ == "__main__":
    main()
