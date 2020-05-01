import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    M = int(rl())
    N = 1
    for _ in range(128):
        N = 2 * N % M
    print(N)


if __name__ == '__main__':
    solve()
