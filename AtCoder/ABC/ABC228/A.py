def main():
    S, T, X = map(int, input().split())
    if S < T:
        print("Yes" if S <= X < T else "No")
    else:
        print("Yes" if S <= X < 24 or 0 <= X < T else "No")


if __name__ == "__main__":
    main()
