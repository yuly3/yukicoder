import sys
from operator import add

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class DualSegmentTree:
    def __init__(self, size: int, segfunc, lazy_ide_ele=0):
        self.lazy_ide_ele = lazy_ide_ele
        self.segfunc = segfunc
        self.N0 = 1 << (size - 1).bit_length()
        self.lazy = [self.lazy_ide_ele] * (2 * self.N0)
    
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
            self.lazy[2 * idx + 1] = self.segfunc(self.lazy[2 * idx + 1], v)
            self.lazy[2 * idx + 2] = self.segfunc(self.lazy[2 * idx + 2], v)
            self.lazy[idx] = self.lazy_ide_ele
    
    def update(self, left: int, right: int, x):
        L = self.N0 + left
        R = self.N0 + right
        
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] = self.segfunc(self.lazy[R - 1], x)
            if L & 1:
                self.lazy[L - 1] = self.segfunc(self.lazy[L - 1], x)
                L += 1
            L >>= 1
            R >>= 1
    
    def query(self, k: int):
        self.propagates(*self.gindex(k, k + 1))
        return self.lazy[k + self.N0 - 1]


def solve():
    N, Q = map(int, rl().split())
    A = list(map(int, rl().split()))
    query = [['A', idx + 1, ai] for idx, ai in enumerate(A)]
    for _ in range(Q):
        c, x, y = rl().split()
        query.append([c, int(x), int(y)])
    
    dual_seg_tree = DualSegmentTree(N, add)
    ans = [0] * N
    for c, x, y in reversed(query):
        x -= 1
        if c == 'B':
            dual_seg_tree.update(x, y, 1)
        else:
            ans[x] += y * dual_seg_tree.query(x)
    print(*ans)


if __name__ == '__main__':
    solve()
