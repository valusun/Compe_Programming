from typing import Tuple


def main():
    N = int(input())
    A = list(map(int, input().split()))

    def ActionCusumPositive(now_sum: int, action_cnt: int, idx: int) -> Tuple[int, int]:
        """累積和を正にするときの動作を行い、操作後の合計値と現在までの操作回数を返す"""
        if now_sum + A[idx] <= 0:
            action_cnt += 1 - (now_sum + A[idx])
            now_sum = 1
        else:
            now_sum += A[idx]
        return (now_sum, action_cnt)

    def ActionCusumNegative(now_sum: int, action_cnt: int, idx: int) -> Tuple[int, int]:
        """累積和を負にするときの動作を行い、操作後の合計値と現在までの操作回数を返す"""
        if now_sum + A[idx] >= 0:
            action_cnt += 1 + (now_sum + A[idx])
            now_sum = -1
        else:
            now_sum += A[idx]
        return (now_sum, action_cnt)

    now_sum = 0
    first_positive_cnt = 0
    for i in range(N):
        if i % 2 == 0:
            now_sum, first_positive_cnt = ActionCusumPositive(
                now_sum, first_positive_cnt, i
            )
        else:
            now_sum, first_positive_cnt = ActionCusumNegative(
                now_sum, first_positive_cnt, i
            )

    now_sum = 0
    first_negative_cnt = 0
    for i in range(N):
        if i % 2 == 0:
            now_sum, first_negative_cnt = ActionCusumNegative(
                now_sum, first_negative_cnt, i
            )
        else:
            now_sum, first_negative_cnt = ActionCusumPositive(
                now_sum, first_negative_cnt, i
            )

    print(min(first_positive_cnt, first_negative_cnt))


if __name__ == "__main__":
    main()
