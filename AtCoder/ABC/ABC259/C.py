def GetListConsecutiveAlphabet(word: str):
    """アルファベットとそれが連続している個数をリスト型にまとめる"""

    ret = [[word[0], 1]]
    for i, s in enumerate(word[1:]):
        if s == word[i]:
            ret[-1][1] += 1
        else:
            ret.append([s, 1])
    return ret


def Check(s: str, t: str, i: int):
    if s[i][0] != t[i][0] or s[i][1] > t[i][1] or (s[i][1] == 1 and t[i][1] > 1):
        return True
    else:
        return False


def main():
    S = input()
    T = input()
    summary_s = GetListConsecutiveAlphabet(S)
    summary_t = GetListConsecutiveAlphabet(T)
    if len(summary_s) != len(summary_t):
        print("No")
        exit()
    for i in range(len(summary_s)):
        if Check(summary_s, summary_t, i):
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
