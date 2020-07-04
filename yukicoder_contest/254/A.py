import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    pos = {ai: idx for idx, ai in enumerate(A)}
    
    left_min = A[:]
    for i in range(1, N):
        left_min[i] = min(left_min[i - 1], left_min[i])
    right_min = A[:]
    for i in range(N - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], right_min[i])
    
    INF = 10 ** 9
    ans = INF
    min_a = right_min[0]
    min_pos = pos[min_a]
    if min_pos != 0 and min_pos != N - 1:
        ans = min_a + left_min[min_pos - 1] + right_min[min_pos + 1]
    
    if min_pos < N - 1:
        for pos_b in range(min_pos + 1, N - 1):
            if right_min[pos_b + 1] < A[pos_b]:
                ans = min(ans, min_a + A[pos_b] + right_min[pos_b + 1])
    
    if 1 < min_pos:
        for pos_b in range(min_pos - 1, 0, -1):
            if left_min[pos_b - 1] < A[pos_b]:
                ans = min(ans, min_a + A[pos_b] + left_min[pos_b - 1])
    print(ans if ans != INF else -1)


if __name__ == '__main__':
    solve()
