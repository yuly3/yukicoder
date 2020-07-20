import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class SegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele):
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.data = [ide_ele] * (2 * self.N0)
        self.segfunc = segfunc
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = self.segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def update(self, k: int, x):
        k += self.N0 - 1
        ################################################################
        self.data[k] = x
        ################################################################
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left: int, right: int):
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        ################################################################
        
        while L < R:
            if L & 1:
                res = self.segfunc(res, self.data[L - 1])
                L += 1
            if R & 1:
                R -= 1
                res = self.segfunc(res, self.data[R - 1])
            L >>= 1
            R >>= 1
        
        ################################################################
        return res


def solve():
    N, Q = map(int, rl().split())
    a = list(map(int, rl().split()))
    query = [list(map(int, rl().split())) for _ in range(Q)]
    
    b = [(ai, i, 1) for i, ai in enumerate(a)]
    c = [(xi, i, 0) for i, (_, _, _, xi) in enumerate(query)]
    q = sorted(b + c, key=itemgetter(0, 2), reverse=True)
    
    f = lambda n, m: (n[0] + m[0], n[1] + m[1])
    ide_ele = (0, 0)
    seg_tree = SegmentTree([ide_ele] * N, f, ide_ele)
    
    ans = [0] * Q
    for val, i, cmd in q:
        if cmd:
            seg_tree.update(i, (val, 1))
        else:
            _, left, right, _ = query[i]
            sm, cnt = seg_tree.query(left - 1, right)
            ans[i] = sm - cnt * val
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
