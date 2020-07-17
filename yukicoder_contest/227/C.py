import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    Q = int(rl())
    
    acc0, acc1 = [0] * N, [0] * N
    for i in range(1, N):
        if A[i - 1] <= A[i]:
            acc0[i] = acc0[i - 1] + 1
        else:
            acc0[i] = acc0[i - 1]
        if A[i] <= A[i - 1]:
            acc1[i] = acc1[i - 1] + 1
        else:
            acc1[i] = acc1[i - 1]
    
    ans = []
    for _ in range(Q):
        left, right = map(int, rl().split())
        f = int(acc0[right] - acc0[left] == right - left)
        g = int(acc1[right] - acc1[left] == right - left)
        ans.append((f, g))
    print('\n'.join(' '.join(map(str, fg)) for fg in ans))


if __name__ == '__main__':
    solve()
