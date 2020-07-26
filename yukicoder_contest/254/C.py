import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    Q = int(rl())
    K = [int(rl()) for _ in range(Q)]
    
    X = 0
    counter = dict()
    cnt_to_x = {0: 0}
    cnt = 0
    while 1:
        cnt += 1
        r = X % N
        X += A[r]
        if r in counter:
            a = counter[r]
            b = cnt - counter[r]
            d = X - cnt_to_x[a]
            break
        else:
            counter[r] = cnt
            cnt_to_x[cnt] = X
    
    ans = []
    for ki in K:
        if ki <= a:
            ans.append(cnt_to_x[ki])
        else:
            roop, rem = divmod(ki - a, b)
            ans.append(roop * d + cnt_to_x[a + rem])
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
