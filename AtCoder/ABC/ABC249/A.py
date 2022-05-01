def CalculateMeter(A, B, C, X):
    ret = 0
    while X > 0:
        if X >= A:
            ret += A * B
            X -= A + C
        else:
            ret += X * B
            break
    return ret


def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = CalculateMeter(A, B, C, X)
    aoki = CalculateMeter(D, E, F, X)
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
