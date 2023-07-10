from collections import Counter
from string import ascii_lowercase

WILDCARDS = {s for s in "atcoder"}


def main():
    S = input()
    T = input()
    s_c = Counter()
    t_c = Counter()
    for s in S:
        s_c[s] += 1
    for t in T:
        t_c[t] += 1
    for a in ascii_lowercase:
        if a == "@":
            continue
        if a in WILDCARDS:
            if s_c[a] == t_c[a]:
                continue
            if s_c[a] > t_c[a]:
                b = s_c[a] - t_c[a]
                if t_c["@"] < b:
                    print("No")
                    exit()
                t_c["@"] -= b
            else:
                b = t_c[a] - s_c[a]
                if s_c["@"] < b:
                    print("No")
                    exit()
                s_c["@"] -= b
        elif s_c[a] != t_c[a]:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
