import strutils, sequtils, math

proc solve() =
    var
        N = stdin.readLine.parseInt
        X = stdin.readLine.split.map(parseInt)
        Y = stdin.readLine.split.map(parseInt)
    
    var d_max = 10 ^ 7
    for i in 0..<N:
        d_max = min(d_max, X[i] + Y[i])
    
    var ans = newSeq[int](N+2)
    ans[^1] = d_max
    for i in 0..<N:
        if X[i] < d_max:
            ans[i+1] = X[i]
        else:
            ans[i+1] = d_max
    
    echo d_max
    echo join(ans, "\n")

solve()
