import heapq
from typing import Counter, List, Union


class MultiSetEx:
    def __init__(self):
        self.elm_counter = Counter()
        self.asc_heapq = []  # popしたときに最大値が取得できる
        self.desc_heapq = []  # popしたときに最小値が取得できる
        self._sum = 0

    def add(self, num: Union[int, List[int]]) -> None:
        """要素を追加する"""
        if isinstance(num, int):
            num = [num]
        for n in num:
            self.elm_counter[n] += 1
            self._sum += n
            heapq.heappush(self.desc_heapq, n)
            heapq.heappush(self.asc_heapq, -n)

    def erase(self, num: int) -> None:
        """要素を削除する"""
        if not self.elm_counter[num]:
            raise KeyError(num)
        self.elm_counter[num] -= 1
        self._sum -= num

    def get_max(self) -> int:
        """要素内の最大値を取得する"""
        p = abs(heapq.heappop(self.asc_heapq))
        while self.elm_counter[p] == 0:
            p = abs(heapq.heappop(self.asc_heapq))
        heapq.heappush(self.asc_heapq, -p)
        return p

    def get_min(self) -> int:
        """要素内の最小値を取得する"""
        p = heapq.heappop(self.desc_heapq)
        while self.elm_counter[p] == 0:
            p = heapq.heappop(self.desc_heapq)
        heapq.heappush(self.desc_heapq, p)
        return p

    def get_sum(self):
        """要素内の合計値を取得する"""
        return self._sum

    def __contains__(self, num):
        return self.elm_counter[num] != 0


def main():
    N, K, Q = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(Q)]
    used = MultiSetEx()
    used.add([0] * K)
    un_used = MultiSetEx()
    un_used.add([0] * (N - K + 1))
    memo = [0] * N
    for x, y in XY:
        bef_val = memo[x - 1]
        memo[x - 1] = y
        min_ = used.get_min()
        max_ = un_used.get_max()
        if bef_val in used:
            if y > max_:
                used.erase(bef_val)
                used.add(y)
            else:
                used.erase(bef_val)
                used.add(max_)
                un_used.erase(max_)
                un_used.add(y)
        else:
            if y < min_:
                un_used.erase(bef_val)
                un_used.add(y)
            else:
                un_used.erase(bef_val)
                un_used.add(min_)
                used.erase(min_)
                used.add(y)
        print(used.get_sum())


if __name__ == "__main__":
    main()
