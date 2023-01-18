def main():
    _, X = map(int, input().split())
    A = set(list(map(int, input().split())))
    print("Yes" if X in A else "No")


if __name__ == "__main__":
    main()
