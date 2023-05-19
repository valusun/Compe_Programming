from collections import deque


def main():
    S = input()
    s = deque(S)
    Q = int(input())
    is_reversed = False
    for _ in range(Q):
        q = list(input().split())
        if q[0] == "1":
            is_reversed = not is_reversed
        else:
            if q[1] == "1":
                if is_reversed:
                    s.append(q[2])
                else:
                    s.appendleft(q[2])
            else:
                if is_reversed:
                    s.appendleft(q[2])
                else:
                    s.append(q[2])
    ans = "".join(s)
    print(ans[::-1] if is_reversed else ans)


if __name__ == "__main__":
    main()
