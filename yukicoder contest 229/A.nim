import sequtils, strutils

proc solve() =
    var N, M, K: int
    (N, M, K) = stdin.readLine.split.map(parseInt)
    var A = mapIt(0..<N, stdin.readLine.split.map(parseInt))

    var dp = newSeq[int](K+1)
    dp[0] = 1
    for i in 0..<N:
        var tmp = newSeq[int](K+1)
        for j in 0..<M:
            for k in 0..K - A[i][j]:
                if dp[k] == 1:
                    tmp[k + A[i][j]] = 1
        dp = tmp
    
    for i in countdown(K, 0):
        if dp[i] == 1:
            echo K - i
            quit()
    
    echo -1

solve()
