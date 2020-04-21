import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    op, *B = rl().split()
    B = list(map(int, B))
    A = [int(rl()) for _ in range(N)]
    
    B.sort()
    if op == '+':
        ans = sum(M - bisect_left(B, K - ai) for ai in A)
    else:
        ans = sum(M - bisect_left(B, -(-K // ai)) for ai in A)
    print(ans)


if __name__ == '__main__':
    solve()
