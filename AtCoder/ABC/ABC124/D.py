from itertools import groupby
from typing import NamedTuple


class EncodeRecord(NamedTuple):
    pattern: str
    cnt: int


def main():
    N, K = map(int, input().split())
    S = input()
    encode_S = [EncodeRecord(k, len(list(v))) for k, v in groupby(S)]
    ans = 0
    left = 0
    res = 0
    zero_cnt = 0
    for right in range(len(encode_S)):
        res += encode_S[right].cnt
        if encode_S[right].pattern == "0":
            zero_cnt += 1
        while K < zero_cnt:
            res -= encode_S[left].cnt
            if encode_S[left].pattern == "0":
                zero_cnt -= 1
            left += 1
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
