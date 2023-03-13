def main():
    N = int(input())
    print("Yes" if len(set([input() for _ in range(N)])) != N else "No")


if __name__ == "__main__":
    main()
