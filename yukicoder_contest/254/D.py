import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class TreeDP:
    def __init__(self, graph, merge, add_root, ide_ele):
        self.graph = graph
        self.merge = merge
        self.add_root = add_root
        self.ide_ele = ide_ele
        self.dp = [ide_ele] * len(graph)
    
    def dfs(self, cur, parent=-1):
        dp_cum = self.ide_ele
        for child in self.graph[cur]:
            if child == parent:
                continue
            dp_cum = self.merge(dp_cum, self.dfs(child, cur))
        self.dp[cur] = self.add_root(dp_cum)
        return self.dp[cur]


def solve():
    N = int(rl())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        v, w = map(lambda u: int(u) - 1, rl().split())
        graph[v].append(w)
        graph[w].append(v)
    
    merge = lambda n, m: [n[0] + m[0] + 1, n[1] + (m[0] + 1) ** 2]
    add_root = lambda n: n
    tree_dp = TreeDP(graph, merge, add_root, [0, 0])
    
    tree_dp.dfs(0)
    ans = []
    for a, b in tree_dp.dp:
        ans.append((a + 1) ** 2 - b)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
