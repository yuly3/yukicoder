import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    if N < K:
        print(-1)
    else:
        print(K - 1)


if __name__ == '__main__':
    solve()
