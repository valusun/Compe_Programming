from collections import Counter
from typing import List
from time import perf_counter
from random import randint


class Solver:
    def __init__(self, D: int, C: List[int], S: List[List[int]]):
        self.period = D
        self.down_points = C
        self.days_points = S
        self.TIME_LIMIT = 1.8
        self.start_time = perf_counter()

    def _calc_score(self, choice_contests: List[int]) -> int:
        score = 0
        contest_id_and_last_day = Counter()
        for now_day, contest_id in enumerate(choice_contests, start=1):
            contest_id_and_last_day[contest_id - 1] = now_day
            score += self.days_points[now_day - 1][contest_id - 1]
            for i in range(26):
                score -= self.down_points[i] * (now_day - contest_id_and_last_day[i])
        return score

    def search_for_local(self) -> None:
        """局所探索法で良いスコアを求める

        Notes:
            - 制限時間内に`contests`を書き換え良いスコアが出れば更新していく
            - 変化させる量が小さすぎると局所最適解に陥ってしまう
                - 多すぎると改善の効率が悪くなってしまう
            - 反復回数を増やすために、計算量を落とす工夫が必要(今の`_calc_score`をどうにかしたい)
        """
        contests = [randint(1, 26) for _ in range(self.period)]
        max_score = self._calc_score(contests)
        while (perf_counter() - self.start_time) < self.TIME_LIMIT:
            new_contests = contests[:]
            idx = randint(0, self.period - 1)
            new_contests[idx] = randint(1, 26)
            score = self._calc_score(new_contests)
            if score > max_score:
                contests = new_contests
                max_score = score
        print(*contests, sep="\n")


def main():
    D = int(input())
    C = list(map(int, input().split()))
    S = [list(map(int, input().split())) for _ in range(D)]
    Solver(D, C, S).search_for_local()


if __name__ == "__main__":
    main()
