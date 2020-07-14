import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, D = map(int, rl().split())
    A = [int(rl()) for _ in range(N)]
    
    B = sorted(A)
    ans = []
    for ai in A:
        idx = bisect_right(B, ai - D)
        ans.append(idx)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
