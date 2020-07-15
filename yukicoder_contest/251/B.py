import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K, X, Y = map(int, rl().split())
    A = [ai - 1 for ai in map(int, rl().split())]
    
    lim = Y // X
    if lim == 0:
        print(-(-max(A) // K))
        return
    
    B = [-(-ai // K) for ai in A]
    B.sort()
    C = B[-lim:]
    
    cnt = 0
    if len(C) != N:
        cnt = B[-(lim + 1)]
    
    ans = cnt * Y
    for ci in C:
        ans += (ci - cnt) * X
    print(ans)


if __name__ == '__main__':
    solve()
