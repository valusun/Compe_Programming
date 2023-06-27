def main():
    N = int(input())
    ans = 0
    for a in range(1, N):
        for b in range(1, N):
            if a * b >= N:
                break
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
