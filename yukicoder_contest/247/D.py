import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    P, K = map(int, rl().split())
    
    dp0 = [0] * (K + 1)
    dp0[0] = 1
    dp1 = [0] * (K + 1)
    for i in range(K):
        dp0[i + 1] = (P + 1) * dp0[i] + 2 * (P - 1) * dp1[i]
        dp0[i + 1] %= MOD
        dp1[i + 1] = dp0[i] + 2 * (P - 1) * dp1[i]
        dp1[i + 1] %= MOD
    print(dp0[K])


if __name__ == '__main__':
    solve()
