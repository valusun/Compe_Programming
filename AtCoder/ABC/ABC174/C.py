def main():
    K = int(input())
    p = 7
    for i in range(K):
        if p % K == 0:
            print(i + 1)
            break
        p = (p * 10 + 7) % K
    else:
        print(-1)


if __name__ == "__main__":
    main()
