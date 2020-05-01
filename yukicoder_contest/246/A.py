import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    if N % 180 == 90:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
