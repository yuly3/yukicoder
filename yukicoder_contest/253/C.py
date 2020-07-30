import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    A.sort(reverse=True)
    ans = 0
    for s in range(1 << (N - 1)):
        mod = K
        for i in range(N - 1):
            if s >> i & 1:
                mod %= A[i]
        mod %= A[-1]
        ans = max(ans, mod)
    print(ans)


if __name__ == '__main__':
    solve()
