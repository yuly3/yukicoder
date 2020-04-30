import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X, Y, Z = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    i = 0
    while 0 < Z and i < N:
        t = min(A[i] // 10000, Z)
        A[i] -= 10000 * t
        Z -= t
        i += 1
    A.sort(reverse=True)
    i = 0
    while 0 < Z and i < N:
        A[i] -= 10000
        Z -= 1
        i += 1
    
    i = 0
    while 0 < Y and i < N:
        if A[i] < 0:
            i += 1
            continue
        t = min(A[i] // 5000, Y)
        A[i] -= 5000 * t
        Y -= t
        i += 1
    A.sort(reverse=True)
    i = 0
    while 0 < Y and i < N:
        A[i] -= 5000
        Y -= 1
        i += 1
    
    cnt = 0
    for ai in A:
        if ai < 0:
            continue
        cnt += -(-(ai + 1) // 1000)
    print('Yes' if cnt <= X else 'No')


if __name__ == '__main__':
    solve()
