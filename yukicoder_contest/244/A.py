import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    D1, D2 = map(int, rl().split())
    
    if D1 == D2 or 2 * D1 == D2:
        print(4)
    elif D1 < D2 < 2 * D1:
        print(8)
    else:
        print(0)


if __name__ == '__main__':
    solve()
