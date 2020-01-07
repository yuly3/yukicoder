import sequtils, strutils

proc solve() =
    var
        N = stdin.readLine.parseInt()
        S = stdin.readLine
        A = stdin.readLine.split.map(parseInt)
        Q = stdin.readLine.parseInt
        K = stdin.readLine.split.map(parseInt)

    var e_acc = @[0]
    for si in S:
        if si == 'E':
            e_acc.add(e_acc[e_acc.len-1] + 1)
        else:
            e_acc.add(e_acc[e_acc.len-1])
    
    for ki in K:
        var
            r = 0
            ans = 0
            k = ki
        for l in 0..<N:
            while r < N and 0 <= k - A[r]:
                k -= A[r]
                inc r
            ans = max(ans, e_acc[r] - e_acc[l])
            if l == r:
                inc r
            else:
                k += A[l]
        echo ans


solve()
