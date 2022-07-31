def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)

    h, w = 0, 0
    i = 0
    while i < N - 1:
        if A[i] == A[i + 1]:
            if h:
                w = A[i]
            else:
                h = A[i]
            i += 2
        else:
            i += 1
        if h and w:
            break
    print(h * w)


if __name__ == "__main__":
    main()
