import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    op, *B = rl().split()
    B = list(map(int, B))
    A = [int(rl()) for _ in range(N)]
    
    ans = 0
    if op == '+':
        for ai in A:
            ans = (ans + ai * M) % K
        for bi in B:
            ans = (ans + bi * N) % K
    else:
        sum_b = sum(B) % K
        for ai in A:
            ans = (ans + ai * sum_b) % K
    print(ans)


if __name__ == '__main__':
    solve()
