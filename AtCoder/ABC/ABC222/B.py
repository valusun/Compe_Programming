def main():
    N, P = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    for i, v in enumerate(A):
        if v >= P:
            print(i)
            break
    else:
        print(N)


if __name__ == "__main__":
    main()
