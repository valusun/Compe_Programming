import numpy as np


class FieldsState:
    def __init__(self, f):
        self.N = len(f)
        self.fields = self._Normalization(np.array(f))

    def _Normalization(self, fields):
        """#を1に、.を0に置き換える。置き換えている場合はそのまま。"""
        return np.where((fields == "#") | (fields == "1"), "1", "0")

    def _GetAmbientStates(self, h, w):
        """自分を含めない周囲8マスの#の数"""
        mn_h, mx_h = max(0, h - 1), min(self.N, h + 2)
        mn_w, mx_w = max(0, w - 1), min(self.N, w + 2)
        black_cnt = np.count_nonzero(self.fields[mn_h:mx_h, mn_w:mx_w] == "1")
        return black_cnt - (self.fields[h][w] == "1")

    def _GetFieldsState(self):
        """周囲8マスに#がいくつあるかの配列を作る"""
        ret = []
        for i in range(self.N):
            tmp = []
            for j in range(self.N):
                tmp.append(self._GetAmbientStates(i, j))
            ret.append(tmp)
        return ret

    def _GetNextFields(self, fields_state):
        """次ターンのフィールド状態を求める"""
        nxt_fields = np.array(self.fields)
        for i in range(self.N):
            for j in range(self.N):
                if self.fields[i][j] == "0":
                    nxt_fields[i][j] = "1" if fields_state[i][j] == 3 else "0"
                else:
                    nxt_fields[i][j] = "1" if 1 < fields_state[i][j] < 4 else "0"
        return nxt_fields

    def ChangeState(self):
        """フィールド状態を次ターンのものにする"""
        fields_states = self._GetFieldsState()
        next_fields = self._GetNextFields(fields_states)
        return FieldsState(next_fields)

    def OutputState(self):
        """状態を出力する"""
        fmt = np.where(self.fields == "0", ".", "#")
        for f in fmt:
            print(*f, sep="")


def main():
    H, X = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    fields_state = FieldsState(fields)
    for _ in range(X):
        fields_state = fields_state.ChangeState()
    fields_state.OutputState()


if __name__ == "__main__":
    main()
