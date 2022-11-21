class FieldsOperator:
    dh = [-1, 0, 1, 0]
    dw = [0, -1, 0, 1]

    def __init__(self, h, w, f):
        self.H = h
        self.W = w
        self.fields = f

    def _GetExistIndex(self, h, w):
        """周囲4マスが存在するインデックスを返す"""
        indexes = [(h, w)]
        for dh, dw in zip(self.dh, self.dw):
            if 0 <= dh + h < self.H and 0 <= dw + w < self.W:
                indexes.append((dh + h, dw + w))
        return indexes

    def _CountBlackSquares(self, h, w):
        squares = [self.fields[nh][nw] for nh, nw in self._GetExistIndex(h, w)]
        print(squares.count("#"))

    def _ReverseSquares(self, h, w):
        for nh, nw in self._GetExistIndex(h, w):
            self.fields[nh][nw] = "#" if self.fields[nh][nw] == "." else "."

    def Command(self):
        return {
            0: self._ReverseSquares,
            1: self._CountBlackSquares,
        }


def main():
    H, W = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    operator = FieldsOperator(H, W, fields)
    Q = int(input())
    for _ in range(Q):
        c, x, y = map(int, input().split())
        operator.Command()[c](x, y)


if __name__ == "__main__":
    main()
