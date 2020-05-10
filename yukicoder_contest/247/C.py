import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    L, R, M, K = map(int, rl().split())
    
    if (L * K - 1) // M != R * K // M:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
