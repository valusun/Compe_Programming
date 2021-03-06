from dataclasses import dataclass, field


@dataclass
class CusumOperator:
    N: int
    A: list[int] = field(default_factory=list)
    now_sum: int = field(init=False, default=0)
    action_cnt: int = field(init=False, default=0)

    def _ManipulateCusumOfIndexToPositive(self, idx) -> None:
        """指定されたインデックスまでの累積和を正にするときの動作を行う"""
        if self.now_sum + self.A[idx] <= 0:
            self.action_cnt += 1 - (self.now_sum + self.A[idx])
            self.now_sum = 1
        else:
            self.now_sum += self.A[idx]

    def _ManipulateCusumOfIndexToNegative(self, idx) -> None:
        """指定されたインデックスまでの累積和を負にするときの動作を行う"""
        if self.now_sum + self.A[idx] >= 0:
            self.action_cnt += 1 + (self.now_sum + self.A[idx])
            self.now_sum = -1
        else:
            self.now_sum += self.A[idx]

    def GetActionCountWhenFirstPositive(self):
        """最初の累積和の符号を正にしたときの操作回数を求める"""
        for i in range(self.N):
            if i % 2 == 0:
                self._ManipulateCusumOfIndexToPositive(i)
            else:
                self._ManipulateCusumOfIndexToNegative(i)

    def GetActionCountWhenFirstNegative(self):
        """最初の累積和の符号を負にしたときの操作回数を求める"""
        for i in range(self.N):
            if i % 2 == 0:
                self._ManipulateCusumOfIndexToNegative(i)
            else:
                self._ManipulateCusumOfIndexToPositive(i)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    first_positive = CusumOperator(N, A)
    first_negative = CusumOperator(N, A)
    first_positive.GetActionCountWhenFirstPositive()
    first_negative.GetActionCountWhenFirstNegative()
    print(min(first_positive.action_cnt, first_negative.action_cnt))


if __name__ == "__main__":
    main()
