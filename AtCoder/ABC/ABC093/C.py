def GetEvenOdd(A):
    odd, even = 0, 0
    for a in A:
        if a % 2:
            odd += 1
        else:
            even += 1
    return odd, even


def main():
    A = list(map(int, input().split()))
    odd, even = GetEvenOdd(A)

    def Increment(tgt):
        for i in range(3):
            if A[i] % 2 == tgt:
                A[i] += 1

    ans = 0
    if odd == 2:
        Increment(1)
        ans += 1
    if even == 2:
        Increment(0)
        ans += 1

    for a in A:
        ans += (max(A) - a) // 2
    print(ans)


if __name__ == "__main__":
    main()
