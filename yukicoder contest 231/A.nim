import sequtils, strutils

proc solve() =
    var A, B, C: float
    (A, B, C) = stdin.readLine.split.map(parseFloat)

    if C == 0:
        echo 0
        quit()
    
    echo A * C / B

solve()
