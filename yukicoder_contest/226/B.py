import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.buffer.readline


class LowestCommonAncestor:
    def __init__(self, tree, root):
        self.n = len(tree)
        self.depth = [0] * self.n
        self.log_size = self.n.bit_length()
        self.parent = [[-1] * self.n for _ in range(self.log_size)]
        
        q = deque([(root, -1, 0)])
        while q:
            v, par, dist = q.pop()
            self.parent[0][v] = par
            self.depth[v] = dist
            for child in tree[v]:
                if child != par:
                    self.depth[child] = dist + 1
                    q.append((child, v, dist + 1))
        
        for k in range(1, self.log_size):
            for v in range(self.n):
                self.parent[k][v] = self.parent[k - 1][self.parent[k - 1][v]]
    
    def query(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        for k in range(self.log_size):
            if self.depth[v] - self.depth[u] >> k & 1:
                v = self.parent[k][v]
        if u == v:
            return u
        
        for k in reversed(range(self.log_size)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][v]
    
    def get_dist(self, u, v):
        ancestor = self.query(u, v)
        return self.depth[u] - self.depth[ancestor] + self.depth[v] - self.depth[ancestor]


def solve():
    N = int(rl())
    graph = [[] for _ in range(N)]
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, rl().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        tree[u].append(v)
        tree[v].append(u)
    
    INF = 10 ** 18
    costs = [INF] * N
    costs[0] = 0
    que = [(0, 0)]
    while que:
        cur, cost = que.pop()
        for child, w in graph[cur]:
            ncost = cost + w
            if costs[child] <= ncost:
                continue
            costs[child] = ncost
            que.append((child, ncost))
    
    lca = LowestCommonAncestor(tree, 0)
    ans = []
    Q = int(rl())
    for _ in range(Q):
        x, y, z = map(int, rl().split())
        ancestor = lca.query(x, y)
        tmp = costs[x] + costs[y] - 2 * costs[ancestor]
        ancestor = lca.query(y, z)
        tmp += costs[y] + costs[z] - 2 * costs[ancestor]
        ancestor = lca.query(z, x)
        tmp += costs[z] + costs[x] - 2 * costs[ancestor]
        tmp //= 2
        ans.append(tmp)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
