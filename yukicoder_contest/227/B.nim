import strutils, sequtils, math

proc solve() =
    var
        N = stdin.readLine.parseInt
        A = newSeq[int](N-1)
        B = newSeq[int](N-1)
    for i in 0..N-2:
        (A[i], B[i]) = stdin.readLine.split.map(parseInt)
    
    var ans = sum(B) + 1
    echo ans

solve()
