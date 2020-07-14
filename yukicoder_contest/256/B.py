import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, H = map(int, rl().split())
    T = list(map(int, rl().split()))
    
    ans = [ti + H for ti in T]
    print(*ans)


if __name__ == '__main__':
    solve()
