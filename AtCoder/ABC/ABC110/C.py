from collections import defaultdict


def main():
    S = input()
    T = input()
    conversion_s = defaultdict(set)
    conversion_t = defaultdict(set)
    for s, t in zip(S, T):
        conversion_s[s].add(t)
        conversion_t[t].add(s)
        if len(conversion_s[s]) == 2 or len(conversion_t[t]) == 2:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
