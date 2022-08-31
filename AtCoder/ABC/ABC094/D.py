def main():
    _ = int(input())
    A = sorted(list(map(int, input().split())))
    ai = A[-1]
    aj = A[0]
    for ak in A[:-1]:
        if abs(ak - ai / 2) <= abs(aj - ai / 2):
            aj = ak
    print(ai, aj)


if __name__ == "__main__":
    main()
