import strutils, sequtils, math, algorithm


proc solve() =
    var N, P: int
    (N, P) = stdin.readLine.split.map(parseInt)
    var a, b, c = newSeq[int](N)
    for i in 0..<N:
        (a[i], b[i], c[i]) = stdin.readLine.split.map(parseInt)
    
    const INF = 5000 * 10 ^ 6
    var dp: array[15004, int]
    dp.fill(INF)
    dp[0] = 0

    for i in 0..<N:
        var dp_tmp = dp
        for j in 0..P:
            if j == 0:
                dp_tmp[j] = dp[j] + a[i]
            elif j == 1:
                dp_tmp[j] = min([dp[j] + a[i], dp[j - 1] + b[i]])
            elif j == 2:
                dp_tmp[j] = min([dp[j] + a[i], dp[j - 1] + b[i], dp[j - 2] + c[i]])
            else:
                dp_tmp[j] = min([dp[j] + a[i], dp[j - 1] + b[i], dp[j - 2] + c[i], dp[j - 3] + 1])
        dp = dp_tmp
    
    var ans = float(dp[P]) / float(N)
    echo ans


when is_main_module:
    solve()
