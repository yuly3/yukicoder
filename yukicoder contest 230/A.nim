import sequtils, strutils

proc solve() =
    var x, y, z: int
    (x, y, z) = stdin.readLine.split.map(parseInt)

    while z != 0:
        if x <= y:
            inc x
        else:
            inc y
        dec z
    echo min(x, y)

solve()
