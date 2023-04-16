import sys
from collections import deque
from typing import List, NamedTuple

sys.setrecursionlimit(10**9)

# 動かしたPCの座標と繋げたPCの座標を格納
moved_roots = []
connected_pc = []

# 4方向の移動
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


class UnionFind:
    def __init__(self, tree_num):
        self.tree_num = tree_num
        self.trees = [-1] * self.tree_num

    def Find(self, x):
        """xの属している木の親を返す"""
        if self.trees[x] < 0:
            return x
        else:
            self.trees[x] = self.Find(self.trees[x])
            return self.trees[x]

    def Union(self, x, y):
        """xが属している木とyが属している木を結合する"""
        x = self.Find(x)
        y = self.Find(y)
        if x == y:
            return
        if self.trees[x] > self.trees[y]:
            x, y = y, x
        self.trees[x] += self.trees[y]
        self.trees[y] = x

    def GetSize(self, x):
        """xが属する木の要素数を返す"""
        return -self.trees[self.Find(x)]

    def IsSame(self, x, y):
        """xとyが同じ木に属しているかを判定する"""
        return self.Find(x) == self.Find(y)


class Coordinate(NamedTuple):
    x: int
    y: int


class ServerRoom:
    def __init__(self, n: int, k: int, f: List[List[str]]):
        self.field_length: int = n
        self.kind_num: int = k
        self.fields: List[List[str]] = f
        self.pc_group = UnionFind(n**2)
        self.no_moved_pc: List[Coordinate] = []

    def IsInField(self, x, y):
        """サーバルーム内か"""
        return 0 <= x < self.field_length and 0 <= y < self.field_length

    def ExistPC(self, x, y):
        """その座標にPCが存在するか"""
        return True if "0" < self.fields[x][y] <= "5" else False

    def IsSamePC(self, fx, fy, tx, ty):
        """与えられた座標にあるPCが同じ種類か"""
        return self.fields[fx][fy] == self.fields[tx][ty]

    def IsSameGroupPC(self, fx, fy, tx, ty):
        """PCが同じグループに属していないか"""
        f_xy = self._GetCoordinateOneDimension(fx, fy)
        t_xy = self._GetCoordinateOneDimension(tx, ty)
        return self.pc_group.IsSame(f_xy, t_xy)

    def CanMovingPC(self, x, y):
        """その座標にあるPCを動かせるか"""
        return (x, y) not in self.no_moved_pc

    def _GetCoordinateOneDimension(self, x, y):
        """座標を1次元に変換したときの数値を返す"""
        return x * self.field_length + y

    def CalcPoint(self, fx, fy, tx, ty):
        """適当な評価関数"""

        f_xy = self._GetCoordinateOneDimension(fx, fy)
        t_xy = self._GetCoordinateOneDimension(tx, ty)
        return self.pc_group.GetSize(f_xy) + self.pc_group.GetSize(t_xy)

    def GetDirections(self, x, y):
        """その場所からどの方向へ移動できるかを返す"""

        directions = []
        pc_kind = self.fields[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not self.IsInField(nx, ny):
                continue
            if pc_kind == self.fields[nx][ny] or self.fields[nx][ny] == "0":
                directions.append([dx[i], dy[i]])
        return directions

    def GetSamePCDirection(self, fx, fy, tx, ty, dir_x, dir_y):
        """決められた方向に進んで同じ種類のPCに辿り着くときの目的地を返す"""

        f = self._GetCoordinateOneDimension(tx, ty)
        pc_kind = self.fields[fx][fy]
        while True:
            next_x, next_y = tx + dir_x, ty + dir_y
            if not self.IsInField(next_x, next_y):
                return -1, -1
            if self.fields[next_x][next_y] == pc_kind:
                next_xy = self._GetCoordinateOneDimension(next_x, next_y)
                if self.pc_group.IsSame(f, next_xy) or fx == next_x and fy == next_y:
                    return -1, -1
                return next_x, next_y
            if self.fields[next_x][next_y] != "0":
                return -1, -1
            tx, ty = next_x, next_y

    def UpdateFieldWhenConnectedCable(self, fx, fy, tx, ty):
        """ケーブルを敷いた時のフィールドを更新する"""

        if fx > tx or fy > ty:
            fx, fy, tx, ty = tx, ty, fx, fy
        if fx == tx:
            dir_x, dir_y, loop_cnt = 0, 1, ty - fy
        else:
            dir_x, dir_y, loop_cnt = 1, 0, tx - fx
        for i in range(loop_cnt - 1):
            if dir_x > dir_y:
                x, y = fx + (i + 1), fy
            else:
                x, y = fx, fy + (i + 1)
            self.fields[x][y] = "9"

    def UpdateMovedData(self, fx, fy, tx, ty):
        """移動した時のデータを更新する"""

        self.fields[tx][ty] = self.fields[fx][fy]
        self.fields[fx][fy] = "0"

    def UpdateConnectedData(self, fx, fy, tx, ty):
        """繋いだ時のデータを更新する"""

        f_xy = self._GetCoordinateOneDimension(fx, fy)
        t_xy = self._GetCoordinateOneDimension(tx, ty)
        self.pc_group.Union(f_xy, t_xy)
        self.no_moved_pc.append(Coordinate(fx, fy))
        self.no_moved_pc.append(Coordinate(tx, ty))


class Worker:
    def __init__(self, n: int, k: int, f: List[List[str]]):
        self.sr: ServerRoom = ServerRoom(n, k, f)
        self.action_limit: int = 100 * k

    def ConnectNeighbor(self):
        """隣接している同じ種類のPCを繋げる"""

        for x in range(self.sr.field_length):
            for y in range(self.sr.field_length):
                if not self.sr.ExistPC(x, y):
                    continue
                for mx, my in [(1, 0), (0, 1)]:
                    next_x = x + mx
                    next_y = y + my
                    if not self.sr.IsInField(next_x, next_y):
                        continue
                    if self.sr.IsSamePC(x, y, next_x, next_y) and self.action_limit:
                        self.Connect(x, y, next_x, next_y)

    def Move(self, roots):
        """PCの移動を行う"""

        for root in roots:
            moved_roots.append(root)
            self.action_limit -= 1
        fx, ft = roots[0][0:2]
        tx, ty = roots[-1][2:]
        self.sr.UpdateMovedData(fx, ft, tx, ty)

    def Connect(self, fx, fy, tx, ty):
        """同じグループに属していないとき、PCを接続する"""

        if self.sr.IsSameGroupPC(fx, fy, tx, ty):
            return
        self.action_limit -= 1
        connected_pc.append([fx, fy, tx, ty])
        self.sr.UpdateConnectedData(fx, fy, tx, ty)

    def _GetPCInfosWhenMovingThreeTimes(self, start_x, start_y):
        """対象のPCを3回まで動かしたときに取り得る消費体力/座標/経路を返す"""

        que = deque()
        que.append((0, start_x, start_y, []))
        visited = set((start_x, start_y))
        pc_moved_infos = []
        while que:
            hp, x, y, roots = que.popleft()
            if hp == 4:
                continue
            pc_moved_infos.append([hp, start_x, start_y, x, y, roots])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if self.sr.IsInField(nx, ny) and self.sr.fields[nx][ny] == "0":
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    nr = roots[:]
                    nr.append([x, y, nx, ny])
                    que.append((hp + 1, nx, ny, nr))
        return pc_moved_infos

    def _GetAllPCMovingInfos(self):
        """PCを動かしたときの座標と移動経路を取得する

        Note:
            [元座標 / 移動先座標 / 経路] を返す
        """

        all_pc_moved_infos = []
        for x in range(self.sr.field_length):
            for y in range(self.sr.field_length):
                if not self.sr.ExistPC(x, y):
                    continue
                if not self.sr.CanMovingPC(x, y):
                    all_pc_moved_infos.append([x, y, x, y, []])
                    continue
                pc_moved_infos = self._GetPCInfosWhenMovingThreeTimes(x, y)
                for info in pc_moved_infos:
                    if info[0] + 1 <= self.action_limit:
                        all_pc_moved_infos.append(info[1:])
        return all_pc_moved_infos

    def _GetPCInfosWhenConnecting(self, moved_infos):
        """移動データから最適な繋ぐ動作を行い、情報を返す

        Note:
            元座標 / 移動先座標 / 接続先座標 / 移動経路
        """

        worked_info = []
        for fx, fy, tx, ty, roots in moved_infos:
            directions = self.sr.GetDirections(tx, ty)
            if not directions:
                continue
            for dir_x, dir_y in directions:
                cx, cy = self.sr.GetSamePCDirection(fx, fy, tx, ty, dir_x, dir_y)
                if cx == cy == -1:
                    continue
                worked_info.append([fx, fy, tx, ty, cx, cy, roots])
        return worked_info

    def DetermineOptimalBehavior(self, infos):
        """接続したときのポイントが一番大きいものを求めて移動と接続を行う"""

        root, connecting = [], []
        max_point = -1
        for info in infos:
            fx, fy, tx, ty = info[2:-1]
            point = self.sr.CalcPoint(fx, fy, tx, ty)
            if point > max_point:
                max_point = point
                root = info[-1]
                connecting = [fx, fy, tx, ty]
        if root:
            self.Move(root)
        self.Connect(*connecting)
        self.sr.UpdateFieldWhenConnectedCable(*connecting)

    def Work(self):
        """全てのPCについて [動かす -> 繋げる -> 最適な動作の決定] を行う"""

        moved_pc_infos = self._GetAllPCMovingInfos()
        worked_infos = self._GetPCInfosWhenConnecting(moved_pc_infos)
        if not worked_infos:
            # 移動も接続も出来なければmainのループ抜けのために0に設定
            self.action_limit = 0
            return
        self.DetermineOptimalBehavior(worked_infos)


def Input():
    """入力の受け取り"""
    N, K = map(int, input().split())
    fields = [list(input()) for _ in range(N)]
    return N, K, fields


def Output(roots, connected):
    """答えの出力"""

    for ans in [roots, connected]:
        print(len(ans))
        for s in ans:
            print(*s)

    # debug用(毎回a.txtの中身を削除しないといけないクソ仕様)
    # def _Write(ans):
    #     with open("a.txt", "a") as f:
    #         f.write(str(len(ans)))
    #         f.write("\n")
    #         for S in ans:
    #             f.write(" ".join(str(s) for s in S))
    #             f.write("\n")

    # _Write(moved_roots)
    # _Write(connected_pc)


def main():
    field_length, pc_kind_num, fields = Input()
    worker = Worker(field_length, pc_kind_num, fields)
    worker.ConnectNeighbor()
    while worker.action_limit:
        worker.Work()
    Output(moved_roots, connected_pc)


if __name__ == "__main__":
    main()
