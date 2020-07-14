import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    N, M, K = map(int, rl().split())
    PQC = [list(map(int, rl().split())) for _ in range(M)]
    
    dp = [[[0] * 301 for _ in range(301)] for _ in range(301)]
    for p, _, _ in PQC:
        dp[1][0][p] = 1
    for i in range(1, N):
        for j in range(K + 1):
            for p, q, c in PQC:
                if K < j + c:
                    continue
                dp[i + 1][j + c][q] += dp[i][j][p]
                dp[i + 1][j + c][q] %= MOD
    print(sum(dp[N][K]) % MOD)


if __name__ == '__main__':
    solve()
