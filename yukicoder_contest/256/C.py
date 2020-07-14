import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    T = list(map(int, rl().split()))
    
    ans = -1
    for D in range(12):
        ds = {d % 12 for d in (D, D + 2, D + 4, D + 5, D + 7, D + 9, D + 11)}
        flg = True
        for ti in T:
            if ti not in ds:
                flg = False
                break
        if flg:
            if ans != -1:
                print(-1)
                return
            ans = D
    print(ans)


if __name__ == '__main__':
    solve()
