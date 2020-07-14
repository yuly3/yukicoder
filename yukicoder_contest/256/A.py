import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A1, A2, A3, A4 = map(int, rl().split())
    if A1 < A2 and A3 > A4:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    solve()
