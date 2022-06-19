def main():
    S = list(input())
    N = len(S)
    my_g, my_p = N // 2 + (N % 2), N // 2
    you_g, you_p = 0, 0
    for s in S:
        if s == "g":
            you_g += 1
        else:
            you_p += 1
    print(min(my_p, you_g) - min(my_g, you_p))


if __name__ == "__main__":
    main()
