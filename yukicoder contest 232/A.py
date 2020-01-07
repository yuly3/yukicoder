def solve():
    S = list(input().split(','))

    if all([1 if s == 'AC' else 0 for s in S]):
        print('Done!')
    else:
        print('Failed...')


if __name__ == '__main__':
    solve()
