import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    x, y, h = map(float, rl().split())
    x *= 1000
    y *= 1000
    
    ans = 0
    while h < x or h < y:
        if h < x and h < y:
            if x <= y:
                x /= 2
            else:
                y /= 2
        elif h < x:
            x /= 2
        elif h < y:
            y /= 2
        h *= 2
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
