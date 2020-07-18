import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = map(int, rl().split())
    
    gcd_ab = gcd(A, B)
    sq = gcd_ab ** 0.5
    if sq.is_integer():
        print('Odd')
    else:
        print('Even')


if __name__ == '__main__':
    solve()
