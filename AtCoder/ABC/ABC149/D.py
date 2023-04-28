def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    T = input()
    my_hand = ""
    ans = 0
    for i, t in enumerate(T):
        if t == "r":
            hand = "p"
            point = p
        elif t == "s":
            hand = "r"
            point = r
        else:
            hand = "s"
            point = s
        if i >= k and my_hand[i - k] == hand:
            hand = "x"
            point = 0
        my_hand += hand
        ans += point
    print(ans)


if __name__ == "__main__":
    main()
