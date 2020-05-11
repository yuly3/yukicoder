import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    Q = int(rl())
    ans = []
    for _ in range(Q):
        N, K = map(int, rl().split())
        if K == 1:
            ans.append(N - 1)
            continue
        sm = 1
        tmp = 1
        depth = 0
        while sm < N:
            tmp *= K
            depth += 1
            sm += tmp
        ans.append(depth)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
