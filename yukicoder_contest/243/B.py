import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _, _ = map(int, rl().split())
    a = deque(map(int, rl().split()))
    S = input()
    
    for si in S:
        if si == 'L':
            tmp = a.popleft()
            a[0] += tmp
            a.append(0)
        else:
            tmp = a.pop()
            a[-1] += tmp
            a.appendleft(0)
    print(*a)


if __name__ == '__main__':
    solve()
