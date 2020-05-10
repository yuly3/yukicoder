import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = map(int, rl().split())
    
    if B == 0:
        print(1)
    elif A == -1:
        print(2)
    else:
        print(-1)


if __name__ == '__main__':
    solve()
