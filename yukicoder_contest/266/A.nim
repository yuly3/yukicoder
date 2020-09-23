import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

proc solve() =
    let N = input().parseInt

    var ans = 0
    for t in 0..100:
        for g in 0..t:
            for pg in 0..100:
                if 5*t + 2*g + 3*pg == N:
                    ans += 1
    echo ans

when is_main_module:
    solve()
