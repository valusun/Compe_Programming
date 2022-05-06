def main():
    A, B, C, D = map(int, input().split())
    if C * D - B <= 0:
        print(-1)
    else:
        blue, red, cnt = A, 0, 0
        while blue > red * D:
            blue += B
            red += C
            cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
