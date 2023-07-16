from collections import Counter
from typing import List


class Solver:
    def __init__(self, D: int, C: List[int], S: List[List[int]]):
        self.period = D
        self.down_points = C
        self.days_points = S

    def _calc_score(self, choice_contests: List[int]) -> int:
        score = 0
        contest_id_and_last_day = Counter()
        for now_day, contest_id in enumerate(choice_contests, start=1):
            contest_id_and_last_day[contest_id - 1] = now_day
            score += self.days_points[now_day - 1][contest_id - 1]
            for i in range(26):
                score -= self.down_points[i] * (now_day - contest_id_and_last_day[i])
        return score

    def _choose_contest_id(self, chosen_contests: List[int]) -> int:
        """その日時点でスコアが最大になるコンテストを選択する

        Args:
            chosen_contests (List[int]): 昨日までに実施したコンテスト一覧

        Returns:
            int: 今日実施するコンテスト
        """
        choice_contest = 1
        max_score = self._calc_score(chosen_contests + [choice_contest])
        for contest in range(2, 27):
            score = self._calc_score(chosen_contests + [contest])
            if score > max_score:
                choice_contest = contest
                max_score = score
        return choice_contest

    def greedy(self) -> None:
        """貪欲にコンテストを選ぶ解法"""
        chosen_contests: List[int] = []
        for _ in range(self.period):
            choice_contest = self._choose_contest_id(chosen_contests)
            chosen_contests.append(choice_contest)
        print(*chosen_contests, sep="\n")


def main():
    D = int(input())
    C = list(map(int, input().split()))
    S = [list(map(int, input().split())) for _ in range(D)]
    Solver(D, C, S).greedy()


if __name__ == "__main__":
    main()
