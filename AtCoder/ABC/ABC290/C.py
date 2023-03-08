def main():
    _, K = map(int, input().split())
    A = set(map(int, input().split()))
    for i in range(K):
        if i not in A:
            print(i)
            break
    else:
        print(K)


if __name__ == "__main__":
    main()
