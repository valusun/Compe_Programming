class Field:
    def __init__(self, h, w, fields):
        self.h = h
        self.w = w
        self.fields = fields
        self.all_black_cnt = self._get_black_cnt()

    def _get_black_cnt(self):
        ret = 0
        for i in range(self.h):
            ret += self.fields[i].count("#")
        return ret

    def push(self, nh, nw):
        for dh, dw in ((-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)):
            next_h = nh + dh
            next_w = nw + dw
            if 0 <= next_h < self.h and 0 <= next_w < self.w:
                is_black = True if self.fields[next_h][next_w] == "#" else False
                self.all_black_cnt += -1 if is_black else 1
                self.fields[next_h][next_w] = "." if is_black else "#"

    def get_num(self):
        print(self.all_black_cnt)


def main():
    H, W = map(int, input().split())
    fields = [list(input()) for _ in range(H)]
    f = Field(H, W, fields)
    Q = int(input())
    for _ in range(Q):
        c, *query = map(int, input().split())
        if c == 0:
            f.push(query[0], query[1])
        else:
            f.get_num()


if __name__ == "__main__":
    main()
