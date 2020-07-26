import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = 0
    for i, ai in enumerate(A):
        ii = i + 1
        ans += ai * ii * (N - ii + 1)
    print(ans)


if __name__ == '__main__':
    solve()
