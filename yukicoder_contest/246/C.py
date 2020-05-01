import sys
from math import log2

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    P, Q = map(int, rl().split())
    
    def check(t):
        taka = t ** 2
        hiku = P + Q * t * log2(t)
        return taka <= hiku
    
    ok, ng = 1., 10 ** 18
    for _ in range(10000):
        mid = (ok + ng) / 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
