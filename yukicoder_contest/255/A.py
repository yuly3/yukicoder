import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    V, T, P = map(int, rl().split())
    
    a = (P + 1) * V
    ans = a + (a - 1) // (T - 1) + 1
    print(ans)


if __name__ == '__main__':
    solve()
