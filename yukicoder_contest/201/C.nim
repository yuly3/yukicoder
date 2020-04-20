import strutils, math


proc solve() =
    var
        N = stdin.readLine.parseInt
        dp: array[1000010, array[10, int]]
    const MOD = 10^9 + 7
    
    dp[0][0] = 1
    for i in 0..<N:
        for j in 0..9:
            for k in j..9:
                dp[i + 1][k] += dp[i][j] mod MOD
    
    var ans = 0
    for i in 0..9:
        ans += dp[N][i] mod MOD
        ans = ans mod MOD
    echo ans


when is_main_module:
    solve()
