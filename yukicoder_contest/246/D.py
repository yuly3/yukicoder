import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    _, _ = map(int, rl().split())
    V = list(map(int, rl().split()))
    R = list(map(int, rl().split()))
    A, B = map(int, rl().split())
    
    N, M = sum(V), sum(R)
    
    dp_v = [0] * (N + 1)
    dp_v[0] = 1
    for vi in V:
        for i in range(N - vi, -1, -1):
            if dp_v[i]:
                dp_v[i + vi] += dp_v[i]
    
    dp_r = [0] * (M + 1)
    dp_r[0] = 1
    for ri in R:
        for i in range(M - ri, -1, -1):
            if dp_r[i]:
                dp_r[i + ri] += dp_r[i]
    
    acc = list(accumulate(dp_v))
    ans = 0
    for idx, val in enumerate(dp_r[1:]):
        i = idx + 1
        if val:
            ans = (ans + (acc[min(N, B * i)] - acc[min(N, A * i - 1)]) * val) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
