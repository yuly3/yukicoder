import strutils, sequtils, math


proc solve() =
    var
        N = stdin.readLine.parseInt
        W = stdin.readLine.split.map(parseInt)
        dp: array[5001, bool]
    
    if sum(W) mod 2 != 0:
        echo "impossible"
        quit()
    
    dp[0] = true
    let target = sum(W) div 2
    for i in 0..<N:
        for w in countdown(target - W[i], 0):
            if dp[w]:
                dp[w + W[i]] = true
    
    if dp[target]:
        echo "possible"
    else:
        echo "impossible"


when is_main_module:
    solve()
