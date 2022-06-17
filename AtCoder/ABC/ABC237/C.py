import re


def GetPrefixCount(s):
    """先頭のaの個数を返す

    Args:
        s (str): 文字列
    """

    return re.match("a*", s).end()


def main():
    S = input()
    first = GetPrefixCount(S)
    last = GetPrefixCount(S[::-1])
    S = "a" * max(0, last - first) + S
    for i in range(len(S) // 2):
        if S[i] != S[-1 - i]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
