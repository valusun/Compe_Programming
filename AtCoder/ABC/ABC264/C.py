def main():
    def DeleteColumnAndCheck(src):
        src = [list(x) for x in zip(*src)]
        for i in range(2**W1):
            res = []
            for j in range(W1):
                if i & (1 << j):
                    res.append(src[j])
            res = [list(x) for x in zip(*res)]
            if res == B:
                print("Yes")
                exit()

    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    for i in range(1, 2**H1):
        res = []
        for j in range(H1):
            if i & (1 << j):
                res.append(A[j])
        DeleteColumnAndCheck(res)
    print("No")


if __name__ == "__main__":
    main()
