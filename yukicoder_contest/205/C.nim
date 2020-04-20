import strutils


proc solve() =
    var
        N = stdin.readLine.parseInt
        dp: array[52, int]
    
    dp[0] = 1
    for i in 0..<N:
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
    echo dp[N]


when is_main_module:
    solve()
