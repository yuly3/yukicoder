import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def eratosthenes(n):
    prime = [2]
    if n == 2:
        return prime
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def solve():
    N = int(rl())
    
    if N == 1:
        print(1)
        return
    
    prime_nums = eratosthenes(10 ** 5 + 1000)
    prime_nums.sort()
    idx = bisect_left(prime_nums, 10 ** 5)
    p = prime_nums[idx:idx + (N + 1)]
    nice_nums = []
    for i, pi in enumerate(p[:-1]):
        for pj in p[i:]:
            nice_nums.append(pi * pj)
    nice_nums.sort()
    print(nice_nums[N - 2])


if __name__ == '__main__':
    solve()
