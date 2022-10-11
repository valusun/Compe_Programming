def GetEvenOddPairCnt(a, b):
    """偶数と奇数のペアの数を求める"""
    if a % 2:
        a += 1
    if b % 2 == 0:
        b -= 1
    return (b - a + 1) // 2


def main():
    A, B = map(int, input().split())
    xor_expr = []

    if A % 2:
        xor_expr.append(A)
    if B % 2 == 0:
        xor_expr.append(B)
    pair = GetEvenOddPairCnt(A, B)
    if pair % 2:
        xor_expr.append(1)

    ans = 0
    for x in xor_expr:
        ans ^= x
    print(ans)


if __name__ == "__main__":
    main()
