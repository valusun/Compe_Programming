def GetSequence(n):
    if n == 1:
        return [1]
    return GetSequence(n - 1) + [n] + GetSequence(n - 1)


def main():
    print(*GetSequence(int(input())))


if __name__ == "__main__":
    main()
