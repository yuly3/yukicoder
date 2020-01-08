import sequtils, strutils

proc solve() =
    var
        N = stdin.readLine.parseInt()
        A = stdin.readLine.split.map(parseInt)
        ans = 1
        flg = true
    
    for i in 1..<N:
        if flg:
            if A[i-1] == A[i]:
                inc ans
            else:
                flg = false
        else:
            inc ans
            flg = true
    echo ans

solve()
