import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    C = rl().rstrip()
    
    ans = 0
    for ci in C[1:]:
        if ci != '0':
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
