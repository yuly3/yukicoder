import strutils, sequtils, math


proc solve() =
    var
        _ = stdin.readLine.parseInt
        A = stdin.readLine.strip.split.map(parseInt)
        dp: array[1 shl 15, int]
    
    dp[0] = 1
    for a in A:
        var dp_tmp = dp
        for i in 0..<dp.len:
            if dp[i] == 1:
                dp_tmp[i xor a] = 1
        dp = dp_tmp
    echo sum(dp)


when is_main_module:
    solve()
