import sys

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
    N, Q = map(int, rl().split())
    a = list(map(int, rl().split()))
    seg_tree = SegmentTree(a, min, 10 ** 7)
    a_to_idx = [0] * (N + 1)
    for i in range(N):
        a_to_idx[a[i]] = i
    
    ans = []
    for _ in range(Q):
        com, left, right = map(int, rl().split())
        left, right = left - 1, right - 1
        if com == 1:
            tmp_l = seg_tree.query(left, left + 1)
            tmp_r = seg_tree.query(right, right + 1)
            a_to_idx[tmp_l] = right
            a_to_idx[tmp_r] = left
            seg_tree.update(right, tmp_l)
            seg_tree.update(left, tmp_r)
        else:
            ans.append(a_to_idx[seg_tree.query(left, right + 1)] + 1)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
