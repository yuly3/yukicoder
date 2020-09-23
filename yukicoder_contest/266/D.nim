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
    ans: seq[int]

proc solve() =
    let N = input().parseInt

    var pi: int
    for _ in 0..<N:
        pi = input().parseInt
        if pi == 2:
            ans.add(2)
        else:
            ans.add((pi - 1)^2)
    echo ans.join("\n")

when is_main_module:
    solve()
