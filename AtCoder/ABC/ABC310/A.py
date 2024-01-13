def main():
    _, P, Q = map(int, input().split())
    D = list(map(int, input().split()))
    print(min(P, Q + min(D)))


if __name__ == "__main__":
    main()
