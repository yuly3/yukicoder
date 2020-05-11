import strutils, math


proc solve() =
    var
        N = stdin.readLine.parseInt
        dp: array[10^6 + 1, int]
    const MOD = 10^9 + 7
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2
    for i in 3..<N:
        dp[i + 1] = (dp[i - 1] + dp[i - 2]) mod MOD
    echo dp[N]


when is_main_module:
    solve()
