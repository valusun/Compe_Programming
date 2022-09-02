def main():
    M, D = map(int, input().split())
    print(M if M <= D else M - 1)


if __name__ == "__main__":
    main()
