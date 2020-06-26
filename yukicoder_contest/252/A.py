import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    p = float(rl())
    print(p / (1 - p))


if __name__ == '__main__':
    solve()
