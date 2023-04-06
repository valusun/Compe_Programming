def main():
    _, X = map(int, input().split())
    A = list(map(int, input().split()))
    tgt = set(A)
    for a in A:
        if X + a in tgt:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()
