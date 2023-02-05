from math import sqrt
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int


class Coord(NamedTuple):
    x: int
    y: int


def IsMoreThan90Degree(base: Coord, p1: Coord, p2: Coord) -> bool:
    """baseの角度が90度以上ならばTrueを返す"""

    v1 = Vector(p1.x - base.x, p1.y - base.y)
    v2 = Vector(p2.x - base.x, p2.y - base.y)
    return v1.x * v2.x + v1.y * v2.y < 0


def GetDistance(p1: Coord, p2: Coord) -> float:
    """最短距離を求める"""

    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def GetArea(p1: Coord, p2: Coord, p3: Coord) -> float:
    """3点で平行四辺形を作成したときの面積を求める"""

    p1_p2 = Vector(p1.x - p2.x, p1.y - p2.y)
    p1_p3 = Vector(p1.x - p3.x, p1.y - p3.y)
    return abs(p1_p2.x * p1_p3.y - p1_p2.y * p1_p3.x)


def main():
    a = Coord(*map(int, input().split()))
    b = Coord(*map(int, input().split()))
    c = Coord(*map(int, input().split()))
    if IsMoreThan90Degree(b, a, c):
        print(GetDistance(a, b))
    elif IsMoreThan90Degree(c, a, b):
        print(GetDistance(a, c))
    else:
        area = GetArea(a, b, c)
        bc_length = GetDistance(b, c)
        print(area / bc_length)


if __name__ == "__main__":
    main()
