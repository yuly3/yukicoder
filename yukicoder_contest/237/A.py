import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    op, *B = rl().split()
    B = list(map(int, B))
    A = [int(rl()) for _ in range(N)]
    
    ans = [[0] * M for _ in range(N)]
    if op == '+':
        for i in range(N):
            for j in range(M):
                ans[i][j] = A[i] + B[j]
    else:
        for i in range(N):
            for j in range(M):
                ans[i][j] = A[i] * B[j]
    for ans_i in ans:
        print(*ans_i)


if __name__ == '__main__':
    solve()
