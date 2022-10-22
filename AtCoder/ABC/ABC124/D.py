from typing import NamedTuple


class EncodeRecord(NamedTuple):
    pattern: str
    cnt: int


def GetRunLengthEncoding(S: str):
    """ランレングス圧縮を行う"""

    pre = S[0]
    cnt = 1
    ret = []
    for s in S[1:]:
        if s == pre:
            cnt += 1
        else:
            ret.append(EncodeRecord(pre, cnt))
            cnt = 1
        pre = s
    ret.append(EncodeRecord(pre, cnt))
    return ret


def main():
    N, K = map(int, input().split())
    S = input()
    encode_S = GetRunLengthEncoding(S)
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
