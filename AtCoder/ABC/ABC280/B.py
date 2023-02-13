def main():
    _ = int(input())
    S = list(map(int, input().split()))
    A = [S[0]]
    for i, s in enumerate(S[1:]):
        A.append(s - S[i])
    print(*A)


if __name__ == "__main__":
    main()
