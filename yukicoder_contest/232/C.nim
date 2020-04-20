import sequtils, strutils

proc solve() =
    var N = stdin.readLine.parseInt()
    var M = N - 1

    var b: seq[int]
    for i in 1..N:
        var question = toSeq(1..N).filterIt(it != i)
        echo "? ", M
        echo join(question, " ")

        var ans = stdin.readLine.parseInt()
        if ans == 0:
            b.add(i)
    echo "! ", b.len
    echo join(b, " ")

solve()
