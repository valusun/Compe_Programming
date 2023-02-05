from math import sqrt
from typing import NamedTuple


class Coord(NamedTuple):
    x: int
    y: int


def GetDistance(c1: Coord, c2: Coord) -> float:
    """最短距離を求める"""

    return sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)


def main():
    N = int(input())
    Coords = [Coord(*map(int, input().split())) for _ in range(N)]
    ans = 10**18
    for i, c1 in enumerate(Coords):
        for c2 in Coords[i + 1 :]:
            ans = min(ans, GetDistance(c1, c2))
    print(ans)


if __name__ == "__main__":
    main()
