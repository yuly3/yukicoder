import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    X, Y = [0] * N, [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, rl().split())
    
    ans = 0
    for i, j in combinations(range(N), 2):
        xi, yi, xj, yj = X[i], Y[i], X[j], Y[j]
        dy = yj - yi
        dx = xj - xi
        if dy == 0:
            ans = max(ans, Y.count(yi))
            continue
        if dx == 0:
            ans = max(ans, X.count(xi))
            continue
        a = dy / dx
        cnt = 2
        for k in range(i + 1, N):
            if j == k:
                continue
            dx = X[k] - xj
            if dx == 0:
                continue
            b = (Y[k] - yj) / dx
            cnt += (a == b)
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    solve()
