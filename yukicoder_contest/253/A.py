import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    N = int(rl())
    A = list(map(int, rl().split()))
    
    for _ in range(N - 1):
        A = [(ai + aj) % MOD for ai, aj in zip(A[:-1], A[1:])]
    print(A[0])


if __name__ == '__main__':
    solve()
