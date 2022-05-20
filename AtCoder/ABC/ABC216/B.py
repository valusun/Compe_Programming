def main():
    N = int(input())
    S = set([input() for _ in range(N)])
    if len(S) == N:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
