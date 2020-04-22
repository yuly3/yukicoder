import sys
from collections import defaultdict
from operator import add

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
    
    def update(self, k, x):
        k += self.N0 - 1
        ################################################################
        self.data[k] = x
        ################################################################
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left, right):
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
    Q, K = map(int, rl().split())
    query = [list(map(int, rl().split())) for _ in range(Q)]
    
    compress = []
    for qi in query:
        if qi[0] == 1:
            compress.append(qi[1])
    compress.sort()
    v_to_idx = {vi: idx for idx, vi in enumerate(compress)}
    counter = defaultdict(int)
    for vi in compress:
        counter[vi] += 1
    N = len(compress)
    
    seg_tree = SegmentTree([0] * N, add, 0)
    ans = []
    for qi in query:
        if qi[0] == 1:
            val = qi[1]
            seg_tree.update(v_to_idx[val] - counter[val] + 1, 1)
            counter[val] -= 1
        else:
            if seg_tree.query(0, N) < K:
                ans.append(-1)
            else:
                ok, ng = N - 1, -1
                while 1 < ok - ng:
                    mid = (ok + ng) // 2
                    if K <= seg_tree.query(0, mid + 1):
                        ok = mid
                    else:
                        ng = mid
                ans.append(compress[ok])
                seg_tree.update(ok, 0)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
