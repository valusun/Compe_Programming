def main():
    N = int(input())
    S = input()
    L, R = [], []
    for i, s in enumerate(S):
        if s == "L":
            R.append(i)
        else:
            L.append(i)
    print(*(L + [N] + R[::-1]))


if __name__ == "__main__":
    main()
