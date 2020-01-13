import strutils, sequtils

proc solve() =
    var A, B, C: int
    (A, B, C) = stdin.readLine.split.map(parseInt)
    var ans = min(min(abs(A-B), abs(B-C)), abs(C-A))
    echo ans

when is_main_module:
    solve()
