def solve():
    N, *P = map(int, open(0).read().split())

    if 0 in P:
        print(0)
        exit()

    ans = 1
    for p in P:
        ans *= p
        ans %= 9

    if ans == 0:
        ans = 9

    print(ans)


if __name__ == '__main__':
    solve()
