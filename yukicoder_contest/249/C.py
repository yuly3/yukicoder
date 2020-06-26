import sys
from collections import Counter, defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X = map(int, rl().split())
    A = [int(rl()) for _ in range(N)]
    
    counter = Counter(A)
    used = defaultdict(int)
    ans = 0
    for ai in A[:-1]:
        used[ai] += 1
        tgt = X ^ ai
        ans += counter[tgt] - used[tgt]
    print(ans)


if __name__ == '__main__':
    solve()
