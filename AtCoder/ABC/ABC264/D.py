from collections import deque


def main():
    S = input()
    tgt = "atcoder"
    seen = set(S)
    Q = deque()
    Q.append((S, 0))
    while Q:
        s, d = Q.popleft()
        if s == tgt:
            print(d)
            break
        for i in range(1, len(s)):
            ns = s[: i - 1] + s[i] + s[i - 1] + s[i + 1 :]
            if ns in seen:
                continue
            seen.add(ns)
            Q.append((ns, d + 1))


if __name__ == "__main__":
    main()
