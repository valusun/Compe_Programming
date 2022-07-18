def main():
    A, B, C = map(int, input().split())
    for a in range(A, A * B + 1, A):
        if a % B == C:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
