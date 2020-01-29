import strutils, sequtils


proc solve() =
    var N, D: int
    (N, D) = stdin.readLine.split.map(parseInt)
    var T, K = newSeq[int](N)
    for i in 0..<N:
        (T[i], K[i]) = stdin.readLine.split.map(parseInt)
    
    var dp: array[101, array[2, int]]
    dp[0][1] = -D
    
    for i in 0..<N:
        dp[i+1][0] = max(dp[i][0] + T[i], dp[i][1] + K[i] - D)
        dp[i+1][1] = max(dp[i][0] + T[i] - D, dp[i][1] + K[i])
    echo max(dp[N])


when is_main_module:
    solve()
