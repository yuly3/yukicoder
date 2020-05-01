import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x: int):
        return -self.parents[self.find(x)]
    
    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def solve():
    N = int(rl())
    uf = UnionFind(N)
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, rl().split())
        uf.union(u, v)
        graph[u].append(v)
        graph[v].append(u)
    
    g_cnt = uf.group_count()
    if g_cnt == 1:
        print('Bob')
    elif g_cnt == 2:
        bridge = False
        for children in graph:
            if len(children) == 1:
                bridge = True
                break
        print('Alice' if bridge else 'Bob')
    else:
        print('Alice')


if __name__ == '__main__':
    solve()
