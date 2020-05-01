import sys
from collections import defaultdict
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    op, *B = rl().split()
    B = list(map(int, B))
    A = [int(rl()) for _ in range(N)]
    
    ans = 0
    if op == '+':
        a_mod = defaultdict(int)
        for ai in A:
            a_mod[ai % K] += 1
        for bi in B:
            ans += a_mod[-bi % K]
    else:
        a_gcd = defaultdict(int)
        b_gcd = defaultdict(int)
        for ai in A:
            a_gcd[gcd(ai, K)] += 1
        for bi in B:
            b_gcd[gcd(bi, K)] += 1
        for key_a, val_a in a_gcd.items():
            for key_b, val_b in b_gcd.items():
                if key_a * key_b % K == 0:
                    ans += val_a * val_b
    print(ans)


if __name__ == '__main__':
    solve()
