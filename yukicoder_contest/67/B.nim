import strutils, sequtils, math


proc solve() =
    var
        N = stdin.readLine.parseInt
        D = stdin.readLine.split.map(parseInt)
        dp: array[2^17, int]
    
    dp[0] = 100
    for S in 0..<2^N:
        if dp[S] == 0:
            continue
        
        var hp_max = 100
        for i in 0..<N:
            if ((S shr i) and 1) == 1 and D[i] < 0:
                hp_max += 100
        
        for i in 0..<N:
            if ((S shr i) and 1) == 0:
                dp[S or (1 shl i)] = max(dp[S or (1 shl i)], min(dp[S] + D[i], hp_max))
    echo dp[2^N - 1]


when is_main_module:
    solve()
