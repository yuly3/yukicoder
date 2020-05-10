import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    A.sort(reverse=True)
    ans = A[0]
    for i in range(1, K):
        if A[i] <= 0:
            break
        ans += A[i]
    print(ans)


if __name__ == '__main__':
    solve()
