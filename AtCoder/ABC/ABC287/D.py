def check(a, b):
    return a == "?" or b == "?" or a == b


def main():
    S = input()
    T = input()
    len_t = len(T)
    pre, suf = [False] * (len_t + 1), [False] * (len_t + 1)
    pre[0] = suf[0] = True
    for i in range(len_t):
        if not check(S[i], T[i]):
            break
        pre[i + 1] = True
    S, T = S[::-1], T[::-1]
    for i in range(len_t):
        if not check(S[i], T[i]):
            break
        suf[i + 1] = True

    for i in range(len_t + 1):
        print("Yes" if pre[i] and suf[len_t - i] else "No")


if __name__ == "__main__":
    main()
