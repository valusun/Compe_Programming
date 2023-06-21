def main():
    D, T, S = map(int, input().split())
    print("Yes" if T >= D / S else "No")


if __name__ == "__main__":
    main()
