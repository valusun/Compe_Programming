def main():
    _, V = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if V in A else "No")


if __name__ == "__main__":
    main()
