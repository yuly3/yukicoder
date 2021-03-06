import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = map(int, rl().split())
    
    if A == B:
        print(A + B - 1)
    else:
        print(min(A, B) * 2)


if __name__ == '__main__':
    solve()
