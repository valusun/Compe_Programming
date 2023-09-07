def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for a, b in zip(A, B):
        cnt += abs(a - b)
    if cnt > K or (K - cnt) % 2 == 1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
