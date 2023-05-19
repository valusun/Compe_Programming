def main():
    A, B = map(int, input().split())
    for n in range(1010):
        if n * 8 // 100 == A and n * 10 // 100 == B:
            print(n)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
