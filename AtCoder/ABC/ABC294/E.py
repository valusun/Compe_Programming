from typing import NamedTuple


class Info(NamedTuple):
    v: int
    l: int


def main():
    _, N, M = map(int, input().split())
    col1 = [Info(*map(int, input().split())) for _ in range(N)]
    col2 = [Info(*map(int, input().split())) for _ in range(M)]
    col1_idx = col2_idx = 0
    ans = 0
    while col1_idx != N and col2_idx != M:
        if col1[col1_idx].v == col2[col2_idx].v:
            ans += min(col1[col1_idx].l, col2[col2_idx].l)
            if col1[col1_idx].l == col2[col2_idx].l:
                col1_idx += 1
                col2_idx += 1
            elif col1[col1_idx].l < col2[col2_idx].l:
                col2[col2_idx] = Info(col2[col2_idx].v, col2[col2_idx].l - col1[col1_idx].l)
                col1_idx += 1
            else:
                col1[col1_idx] = Info(col1[col1_idx].v, col1[col1_idx].l - col2[col2_idx].l)
                col2_idx += 1
        else:
            if col1[col1_idx].l < col2[col2_idx].l:
                col2[col2_idx] = Info(col2[col2_idx].v, col2[col2_idx].l - col1[col1_idx].l)
                col1_idx += 1
            else:
                col1[col1_idx] = Info(col1[col1_idx].v, col1[col1_idx].l - col2[col2_idx].l)
                col2_idx += 1
    print(ans)


if __name__ == "__main__":
    main()
