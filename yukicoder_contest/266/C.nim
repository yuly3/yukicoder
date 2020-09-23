import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

var
    A: seq[int]
    dp: array[200010, array[10, int]]

proc solve() =
    let N = input().parseInt
    A = input().split.map(parseInt)

    dp[0][0] = 1
    for i in 0..<N:
        for j in 0..9:
            if 0 < dp[i][j]:
                dp[i + 1][j].chmax(dp[i][j])
                dp[i + 1][(j + A[i]) mod 10].chmax(dp[i][j] + 1)
    echo dp[N][0] - 1

when is_main_module:
    solve()
