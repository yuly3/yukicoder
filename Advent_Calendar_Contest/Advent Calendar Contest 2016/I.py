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
    N = int(input())
    
    if N == 1:
        print(-1)
        exit()
    
    primes = eratosthenes(N)
    dp = [0] + [-1] * N
    
    for p_num in primes:
        for i in range(N, -1, -1):
            if i - p_num < 0:
                break
            if dp[i - p_num] != -1:
                dp[i] = max(dp[i], dp[i - p_num] + 1)
    print(dp[N])


if __name__ == '__main__':
    solve()
