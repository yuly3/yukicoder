import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = 0
    for i, j in combinations(range(N), 2):
        ans = max(ans, A[i] ^ A[j])
    print(ans)


if __name__ == '__main__':
    solve()
