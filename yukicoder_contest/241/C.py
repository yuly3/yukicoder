import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, d, K = map(int, rl().split())
    MOD = 10 ** 9 + 7
    
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        acc = 0
        for j in range(K):
            acc = (acc + dp[i - 1][j]) % MOD
            if d <= j:
                acc = (acc - dp[i - 1][j - d]) % MOD
            dp[i][j + 1] = acc
    print(dp[N][K])


if __name__ == '__main__':
    solve()
