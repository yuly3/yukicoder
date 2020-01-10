import strutils

proc solve() =
    var S = stdin.readLine
    for i in 0..<S.len:
        if i mod 2 == 0 and not isLowerAscii(S[i]):
            echo "No"
            quit()
        elif i mod 2 == 1 and S[i] != ' ':
            echo "No"
            quit()
    echo "Yes"

solve()
