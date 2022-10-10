from typing import NamedTuple
import numpy as np


class Coordinate(NamedTuple):
    x: int
    y: int


def main():
    C = [Coordinate(*map(int, input().split())) for _ in range(4)]
    vector = [
        Coordinate(C[1].x - C[0].x, C[1].y - C[0].y),
        Coordinate(C[2].x - C[1].x, C[2].y - C[1].y),
        Coordinate(C[3].x - C[2].x, C[3].y - C[2].y),
        Coordinate(C[0].x - C[3].x, C[0].y - C[3].y),
    ]
    outer_product = [
        np.cross(vector[0], vector[1]),
        np.cross(vector[1], vector[2]),
        np.cross(vector[2], vector[3]),
        np.cross(vector[3], vector[0]),
    ]

    print("No" if min(outer_product) < 0 else "Yes")


if __name__ == "__main__":
    main()
