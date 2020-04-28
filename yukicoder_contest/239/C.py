import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, init_value: list, segfunc, ide_ele=0, lazy_ide_ele=0):
        self.ide_ele = ide_ele
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        n = len(init_value)
        self.N0 = 1 << (n - 1).bit_length()
        self.data = [self.ide_ele] * (2 * self.N0)
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
        
        for i, x in enumerate(init_value):
            self.data[i + self.N0 - 1] = x
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def gindex(self, left, right):
        L = left + self.N0
        R = right + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1
        while L:
            yield L
            L >>= 1
    
    def propagates(self, *ids):
        for i in reversed(ids):
            idx = i - 1
            v = self.lazy[idx]
            if v == self.lazy_ide_ele:
                continue
            ################################################################
            self.data[2 * idx + 1] += v
            self.data[2 * idx + 2] += v
            self.lazy[2 * idx + 1] += v
            self.lazy[2 * idx + 2] += v
            ################################################################
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left, right, x):
        ids = tuple(self.gindex(left, right))
        ################################################################
        # self.propagates(*ids)
        ################################################################
        L = self.N0 + left
        R = self.N0 + right
        
        while L < R:
            if R & 1:
                R -= 1
                ################################################################
                self.lazy[R - 1] += x
                self.data[R - 1] += x
                ################################################################
            if L & 1:
                ################################################################
                self.lazy[L - 1] += x
                self.data[L - 1] += x
                ################################################################
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            idx = i - 1
            self.data[idx] = self.segfunc(self.data[2 * idx + 1], self.data[2 * idx + 2]) + self.lazy[idx]
    
    def query(self, left, right):
        self.propagates(*self.gindex(left, right))
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
    A = list(map(int, rl().split()))
    query = [['A', idx + 1, ai] for idx, ai in enumerate(A)]
    for _ in range(Q):
        c, x, y = rl().split()
        query.append([c, int(x), int(y)])
    
    segfunc = lambda _, b: b
    lazy_seg_tree = LazySegmentTree([0] * N, segfunc)
    
    ans = [0] * N
    for c, x, y in reversed(query):
        x -= 1
        if c == 'B':
            lazy_seg_tree.update(x, y, 1)
        else:
            ans[x] += y * lazy_seg_tree.query(x, x + 1)
    print(*ans)


if __name__ == '__main__':
    solve()
