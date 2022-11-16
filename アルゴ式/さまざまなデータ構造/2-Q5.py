def main():
    N = int(input())
    A = list(range(N))
    while len(A) != 1:
        del A[0]
        A.append(A.pop(0))
    print(A[0] + 1)


if __name__ == "__main__":
    main()
