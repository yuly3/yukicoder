import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    Y = list(map(int, rl().split()))
    
    dp = [[0] * (10 ** 4 + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i + 1][0] = dp[i][0] + Y[i]
        for j in range(1, 10 ** 4 + 1):
            dp[i + 1][j] = min(dp[i + 1][j - 1], dp[i][j] + abs(j - Y[i]))
    print(min(dp[N]))


if __name__ == '__main__':
    solve()
