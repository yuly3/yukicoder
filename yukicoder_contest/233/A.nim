import strutils

proc solve() =
    var
        N = stdin.readLine.parseInt
        ans = ""
    if N == 1:
        echo 1
        quit()
    for i in countdown(N-1, 0):
        for _ in 0..<N:
            ans &= $i
    echo ans

when is_main_module:
    solve()
